import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from data_utils import read_all_csv_in_folder, flatten_dict, write_dict_to_csv

FOLDER_PATH = "./csv_data"

class CSVCompareApp:
    def __init__(self, master):
        self.master = master
        self.all_data = read_all_csv_in_folder(FOLDER_PATH)
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
            show="headings",
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

        self.checkbox_states = {}
        for _, row in df.iterrows():
            values = list(row)
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
                "",
                tk.END,
                values=[select_symbol] + values,
                tags=("diff",) if diff else ()
            )
            self.checkbox_states[item_id] = False

        self.tree.bind("<Button-1>", self.toggle_checkbox)
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
        """Kliknięcie w kolumnę Select przełącza stan checkboxa."""
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return

        col = self.tree.identify_column(event.x)
        if col != "#1":  # tylko pierwsza kolumna ("Select")
            return

        row_id = self.tree.identify_row(event.y)
        if not row_id:
            return

        current = self.checkbox_states.get(row_id, False)
        new_state = not current
        self.checkbox_states[row_id] = new_state

        values = list(self.tree.item(row_id, "values"))
        values[0] = "☑" if new_state else "☐"
        self.tree.item(row_id, values=values, tags=("checked",) if new_state else ())

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
            var_name = values[1]
            base_value = values[2]  # kolumna po Variable

            for t_idx, t_col in enumerate(target_cols, start=3):
                values[t_idx] = base_value

            self.tree.item(row_id, values=values)
            copied += 1

        messagebox.showinfo("Kopiowanie zakończone",
                            f"Skopiowano {copied} zmiennych z {base_col} do pozostałych plików.")

    def save_changes(self):
        """Zapisuje bieżące dane z tabeli do plików CSV z użyciem write_dict_to_csv()."""
        if not self.selected_files:
            messagebox.showwarning("Brak plików", "Nie wybrano żadnych plików do zapisu.")
            return

        try:
            # Pobierz wszystkie wiersze z Treeview
            rows = []
            for row_id in self.tree.get_children():
                row_values = list(self.tree.item(row_id, "values"))
                rows.append(row_values)

            # Kolumny (pomijamy "Select")
            columns = self.tree["columns"][1:]  # ["Variable", "file1", "file2", ...]

            df = pd.DataFrame(rows, columns=["Select"] + list(columns))
            df = df.drop(columns=["Select"])

            # Folder z plikami CSV
            folder = "./csv_data"
            os.makedirs(folder, exist_ok=True)

            # Zapisz zmiany dla każdego pliku
            for col in df.columns[1:]:
                file_path = os.path.join(folder, col)

                # Zamiana dataframe na słownik {zmienna: wartość}
                data_dict = dict(zip(df["Variable"], df[col]))

                # Użycie Twojej funkcji z data_utils
                write_dict_to_csv(data_dict, file_path)

            messagebox.showinfo("Zapis zakończony", f"✅ Zapisano zmiany do {len(df.columns) - 1} plików CSV.")

        except Exception as e:
            messagebox.showerror("Błąd zapisu", f"❌ Wystąpił błąd podczas zapisu:\n{e}")