import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os
import re
import sys
from data_utils import read_all_csv_in_folder, flatten_dict, write_dict_to_csv

if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS  # folder tymczasowy PyInstaller
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Domyślnie brak folderu CSV – użytkownik wybiera go ręcznie
FOLDER_PATH = None

print("BASE_PATH:", BASE_PATH)

class CSVCompareApp:
    def __init__(self, master):
        self.master = master
        self.all_data = read_all_csv_in_folder(FOLDER_PATH) if FOLDER_PATH and os.path.isdir(FOLDER_PATH) else {}
        self.selected_files = []
        self.df = None
        self.tree = None

        # --- GÓRNY PANEL ---
        top_frame = tk.Frame(master, bg="#343a40")
        top_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(top_frame, text="CSV Comparison Tool",
                 fg="white", bg="#343a40", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=10)

        # Wybór pliku do dodania
        self.file_combo = ttk.Combobox(top_frame, values=list(self.all_data.keys()), state="readonly")
        self.file_combo.pack(side=tk.LEFT, padx=5)

        tk.Button(top_frame, text="➕ Dodaj plik", command=self.add_file, bg="#007bff", fg="white").pack(side=tk.LEFT,
                                                                                                        padx=5)
        tk.Button(top_frame, text="➖ Usuń plik", command=self.remove_file, bg="#dc3545", fg="white").pack(side=tk.LEFT,
                                                                                                          padx=5)
        tk.Button(top_frame, text="🔄 Odśwież", command=self.show_table, bg="#17a2b8", fg="white").pack(side=tk.LEFT,
                                                                                                       padx=5)
        tk.Button(top_frame, text="💾 Zapisz zmiany", command=self.save_changes, bg="#28a745", fg="white").pack(
            side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="📂 Wybierz folder CSV", command=self.select_folder,
                  bg="#ffc107", fg="black").pack(side=tk.LEFT, padx=5)

        # ✅ Checkbox: Ukryj identyczne wartości
        self.hide_identical_var = tk.BooleanVar(value=False)
        self.hide_identical_check = tk.Checkbutton(
            top_frame,
            text="Ukryj identyczne wartości",
            variable=self.hide_identical_var,
            bg="#343a40",
            fg="white",
            selectcolor="#343a40",
            activebackground="#343a40",
            command=self.show_table
        )
        self.hide_identical_check.pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(top_frame, text="", fg="white", bg="#343a40")
        self.status_label.pack(side=tk.RIGHT, padx=10)

        # --- PANEL LISTY WYBRANYCH PLIKÓW ---
        middle_frame = tk.Frame(master, bg="#f0f0f0")
        middle_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(middle_frame, text="Wybrane pliki:", bg="#f0f0f0").pack(anchor="w")

        self.active_files_list = tk.Listbox(middle_frame, selectmode=tk.SINGLE, height=5)
        self.active_files_list.pack(fill=tk.X, padx=5, pady=2)

        # --- RAMKA NA TABELĘ ---
        self.table_frame = tk.Frame(master)
        self.table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    # ------------------- LOGIKA -------------------

    def add_file(self):
        file = self.file_combo.get()
        if not file:
            messagebox.showinfo("Brak pliku", "Wybierz plik z listy, zanim go dodasz.")
            return
        if file not in self.selected_files:
            self.selected_files.append(file)
            self.active_files_list.insert(tk.END, file)
            self.status_label.config(text=f"Dodano: {file}")
            self.show_table()
        else:
            messagebox.showinfo("Info", f"Plik '{file}' już jest w tabeli.")

    def remove_file(self):
        selected = self.active_files_list.curselection()
        if not selected:
            messagebox.showinfo("Brak wyboru", "Zaznacz plik na liście, który chcesz usunąć.")
            return
        index = selected[0]
        file_to_remove = self.selected_files[index]
        self.selected_files.remove(file_to_remove)
        self.active_files_list.delete(index)
        self.status_label.config(text=f"Usunięto: {file_to_remove}")
        self.show_table()

    def show_table(self):
        if not FOLDER_PATH or not os.path.isdir(FOLDER_PATH):
            messagebox.showwarning("Brak folderu", "Najpierw wybierz folder z plikami CSV.")
            return       # --- odśwież listę plików ---

        self.all_data = read_all_csv_in_folder(FOLDER_PATH)
        self.file_combo['values'] = list(self.all_data.keys())

        if not self.selected_files:
            if self.tree:
                self.tree.destroy()
            self.status_label.config(text="Brak plików do porównania.")
            return

        base_file = self.selected_files[0]
        base_flat = flatten_dict(self.all_data.get(base_file, {}))
        df = pd.DataFrame(list(base_flat.items()), columns=["Variable", base_file])

        for filename in self.selected_files[1:]:
            flat = flatten_dict(self.all_data.get(filename, {}))
            df_temp = pd.DataFrame(list(flat.items()), columns=["Variable", filename])
            df = pd.merge(df, df_temp, on="Variable", how="outer")

        df = df.fillna("")

        # --- 🔹 FILTROWANIE: ukryj identyczne wartości ---
        if self.hide_identical_var.get():
            mask = df.apply(
                lambda row: len(set(str(v) for v in row[1:])) > 1, axis=1
            )
            df = df[mask]

        self.df = df

        # Usuń starą tabelę
        if hasattr(self, "table_container"):
            self.table_container.destroy()

        self.table_container = tk.Frame(self.table_frame)
        self.table_container.pack(fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.table_container, orient="vertical")
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        cols = ["Select"] + list(df.columns)
        self.tree = ttk.Treeview(
            self.table_container,
            columns=cols,
            show="tree headings",
            selectmode="none",
            yscrollcommand=self.scrollbar_y.set
        )
        self.scrollbar_y.config(command=self.tree.yview)

        self.tree.heading("Select", text="✔")
        self.tree.column("Select", width=40, anchor="center")

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="w")

        self.tree.tag_configure("diff", background="#ffcccc")
        self.tree.tag_configure("checked", background="#ccffcc")

        # --- Checkboxy i dane z hierarchią ---
        self.checkbox_states = {}
        tree_nodes = {}  # cache do przechowywania ścieżek

        for _, row in df.iterrows():
            values = list(row)
            variable_full = values[0]

            # 🔹 Rozbij po kropkach, ale zachowaj indeksy [x,y] jako osobne poziomy
            parts = re.split(r'\.(?![^[]*\])', variable_full)  # dzieli po '.' ale nie wewnątrz nawiasów
            expanded_parts = []

            for p in parts:
                # jeżeli zawiera indeks np. "iRobotMIGSteps[1,0]"
                match = re.match(r"([^\[]+)(\[.*\])", p)
                if match:
                    expanded_parts.append(match.group(1))  # np. "iRobotMIGSteps"
                    expanded_parts.append(match.group(2))  # np. "[1,0]"
                else:
                    expanded_parts.append(p)

            parent = ""
            full_path = ""

            # --- hierarchiczne tworzenie węzłów ---
            for level in expanded_parts[:-1]:
                full_path = full_path + "." + level if full_path else level
                if full_path not in tree_nodes:
                    node_id = self.tree.insert(parent, "end", text=level, values=["☐", ""], open=False)
                    tree_nodes[full_path] = node_id
                    self.checkbox_states[node_id] = False
                parent = tree_nodes[full_path]

            # --- ostatni poziom (zmienna końcowa) ---
            var_name = expanded_parts[-1]
            ref_value = None
            diff = False
            for val in values[1:]:
                if ref_value is None:
                    ref_value = val
                elif str(val) != str(ref_value):
                    diff = True
                    break

            select_symbol = "☐"
            item_id = self.tree.insert(
                parent,
                "end",
                text=var_name,
                values=[select_symbol] + values,
                tags=("diff",) if diff else ()
            )
            self.checkbox_states[item_id] = False

        # --- Tutaj dodajemy bind na edycję ---
        self.tree.bind("<Button-1>", self.toggle_checkbox)
        self.tree.bind("<Double-1>", self.edit_cell)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Aktualizacja statusu
        total = len(flatten_dict(self.all_data.get(base_file, {})))
        visible = len(df)
        self.status_label.config(
            text=f"Porównano {len(self.selected_files)} plików, wyświetlono {visible}/{total} zmiennych."
        )

        # --- Przyciski akcji (kopiuj + zapisz) ---
        # Usuwamy stare przyciski, jeśli istnieją
        if hasattr(self, "buttons_frame"):
            self.buttons_frame.destroy()

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.copy_button = tk.Button(
            self.buttons_frame,
            text="📋 Kopiuj zaznaczone zmienne →",
            bg="#007bff",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.copy_selected
        )
        self.copy_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(
            self.buttons_frame,
            text="💾 Zapisz zmiany do CSV",
            bg="#28a745",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.save_changes
        )
        self.save_button.pack(side=tk.LEFT, padx=10)

        if self.hide_identical_var.get():
            # filtruj tylko wiersze z różnicami
            df_filtered = []
            for _, row in df.iterrows():
                vals = row[1:].astype(str).tolist()
                if len(set(vals)) > 1:
                    df_filtered.append(row)
            df = pd.DataFrame(df_filtered, columns=df.columns)

    def toggle_checkbox(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return

        col = self.tree.identify_column(event.x)
        if col != "#1":
            return

        row_id = self.tree.identify_row(event.y)
        if not row_id:
            return

        # przełącz stan checkboxa
        current = self.checkbox_states.get(row_id, False)
        new_state = not current
        self.checkbox_states[row_id] = new_state

        # Zaktualizuj symbol
        values = list(self.tree.item(row_id, "values"))
        values[0] = "☑" if new_state else "☐"
        self.tree.item(row_id, values=values)

        # Jeśli węzeł ma dzieci, zaznacz/odznacz wszystkie dzieci rekurencyjnie
        def set_children(node, state):
            for child in self.tree.get_children(node):
                self.checkbox_states[child] = state
                child_vals = list(self.tree.item(child, "values"))
                child_vals[0] = "☑" if state else "☐"
                self.tree.item(child, values=child_vals)
                set_children(child, state)

        set_children(row_id, new_state)

    def copy_selected(self):
        """Kopiuj dane z kolumny 1 (pierwszy plik) do pozostałych dla zaznaczonych zmiennych."""
        if not self.selected_files or len(self.selected_files) < 2:
            messagebox.showwarning("Brak plików", "Wybierz przynajmniej 2 pliki do porównania.")
            return

        base_col = self.selected_files[0]
        target_cols = self.selected_files[1:]

        copied = 0
        for row_id, checked in self.checkbox_states.items():
            if not checked:
                continue

            values = list(self.tree.item(row_id, "values"))
            # pomiń węzły nadrzędne, które nie mają wszystkich kolumn
            if len(values) < 3:
                continue

            var_name = values[1]
            base_value = values[2]  # kolumna po Variable

            for t_idx, t_col in enumerate(target_cols, start=3):
                values[t_idx] = base_value

            self.tree.item(row_id, values=values)
            copied += 1

        messagebox.showinfo("Kopiowanie zakończone",
                            f"Skopiowano {copied} zmiennych z {base_col} do pozostałych plików.")

    def save_changes(self):
        if not self.selected_files:
            messagebox.showwarning("Brak plików", "Nie wybrano żadnych plików do zapisu.")
            return

        try:
            # 1) Odbuduj pełny DataFrame z self.all_data
            base_file = self.selected_files[0]
            base_flat_full = flatten_dict(self.all_data.get(base_file, {}))
            full_df = pd.DataFrame(list(base_flat_full.items()), columns=["Variable", base_file])

            for filename in self.selected_files[1:]:
                flat = flatten_dict(self.all_data.get(filename, {}))
                df_temp = pd.DataFrame(list(flat.items()), columns=["Variable", filename])
                full_df = pd.merge(full_df, df_temp, on="Variable", how="outer")

            full_df = full_df.fillna("")

            # 2) Przygotuj słowniki do zapisu
            file_value_maps = {}
            for col in full_df.columns[1:]:
                file_value_maps[col] = dict(zip(full_df["Variable"], full_df[col].astype(str)))

            # 3) Funkcja rekurencyjna do przeglądania wszystkich węzłów
            def update_values(node_id):
                vals = list(self.tree.item(node_id, "values"))
                if len(vals) < 3:
                    # węzeł nadrzędny -> idź do dzieci
                    for child in self.tree.get_children(node_id):
                        update_values(child)
                    return

                variable = vals[1]
                for idx, filename in enumerate(list(full_df.columns[1:]), start=2):
                    new_val = vals[idx]
                    file_value_maps[filename][variable] = str(new_val)

            # wywołanie dla wszystkich korzeni
            for root in self.tree.get_children():
                update_values(root)

            # 4) Zapis do CSV
            folder = FOLDER_PATH
            os.makedirs(folder, exist_ok=True)

            for filename, mapping in file_value_maps.items():
                file_path = os.path.join(folder, filename)
                write_dict_to_csv(mapping, file_path)

            messagebox.showinfo("Zapis zakończony", f"✅ Zapisano zmiany do {len(self.selected_files)} plików CSV.")

        except Exception as e:
            messagebox.showerror("Błąd zapisu", f"❌ Wystąpił błąd podczas zapisu:\n{e}")

    def edit_cell(self, event):
        """Pozwala edytować wartość po dwukliku w komórkę (ale nie kolumnę #0 ani checkbox)."""
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return

        col = self.tree.identify_column(event.x)
        if col in ("#0", "#1"):  # <--- NIE EDYTUJ kolumny hierarchii ani checkboxa
            return

        row_id = self.tree.identify_row(event.y)
        if not row_id:
            return

        x, y, width, height = self.tree.bbox(row_id, col)
        value = self.tree.set(row_id, column=col)

        entry = tk.Entry(self.tree)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, value)
        entry.focus()

        def save_edit(event):
            new_value = entry.get()
            self.tree.set(row_id, column=col, value=new_value)
            entry.destroy()

        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", lambda e: entry.destroy())

    def select_folder(self):
        folder_selected = filedialog.askdirectory(title="Wybierz folder z plikami CSV")
        if folder_selected:
            global FOLDER_PATH
            FOLDER_PATH = folder_selected  # aktualizujemy ścieżkę
            self.all_data = read_all_csv_in_folder(FOLDER_PATH)
            self.file_combo['values'] = list(self.all_data.keys())
            self.status_label.config(text=f"Wybrano folder: {FOLDER_PATH}")
            self.show_table()

            print("BASE_PATH:", BASE_PATH)
            print("FOLDER_PATH:", FOLDER_PATH)