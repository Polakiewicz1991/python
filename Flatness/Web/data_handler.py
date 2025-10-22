import pandas as pd
import io
import base64
import os
import tkinter as tk
from tkinter import filedialog

def parse_csv(contents_or_path, sep=';'):
    # jeśli dane pochodzą z uploadu Dash (base64)
    if isinstance(contents_or_path, str) and contents_or_path.startswith("data:"):
        content_type, content_string = contents_or_path.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), sep=sep)
    # jeśli podano ścieżkę do pliku
    elif os.path.exists(contents_or_path):
        try:
            df = pd.read_csv(contents_or_path, sep=sep, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(contents_or_path, sep=sep, encoding='cp1250')  # dla polskich znaków
    else:
        raise ValueError("Niepoprawne wejście: ani base64, ani istniejąca ścieżka")

    # opcjonalnie: walidacja kolumn, typów, usuwanie NULL
    # df = df.dropna()  # np. usunięcie pustych wierszy
    return df

# def choose_folder():
#     print("test")
#     root = tk.Tk()
#     root.withdraw()
#     folder = filedialog.askdirectory(title="Wybierz folder z plikami CSV")
#     return folder