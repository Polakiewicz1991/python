import csv
import os
import re

def read_csv_to_nested_dict(file_path):
    """
    Wczytuje CSV i zwraca płaski słownik:
    {
        "GVL_Reference.MAP.iRobotPlasmaSteps[1, 0]": 2,
        "GVL_Reference.MAP.iRobotPlasmaSteps[1, 1]": 2,
        ...
    }
    """
    data = {}
    with open(file_path, newline='',  encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) != 2:
                continue
            key = row[0].strip()
            value = row[1].strip()

            # Konwersja numeryczna, jeśli możliwa
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass

            data[key] = value
    return data

def read_all_csv_in_folder(folder_path):
    all_data = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            all_data[filename] = read_csv_to_nested_dict(file_path)
    return all_data


def flatten_dict(d, parent_key="", sep="."):
    """Flatten nested dictionaries for tabular display"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def write_dict_to_csv(data, file_path):
    """
    Zapisuje słownik w formacie 1:1 jak wczytany:
    GVL_Reference.MAP.iRobotPlasmaSteps[1, 0];2
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        for key, value in data.items():
            writer.writerow([key, value])

def save_dict_to_csv(data_dict, file_path):
    """
    Zapisuje dane słownika do pliku CSV w formacie:
    nazwa_zmiennej;wartość
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        for key, value in data_dict.items():
            writer.writerow([key, value])

def read_csv_preserve_order(file_path):
    """
    Wczytuje CSV w oryginalnej kolejności jako listę:
    [("key", "value"), ...]  # value jako str, nic nie konwertujemy
    """
    rows = []
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) == 2:
                rows.append((row[0], row[1]))
    return rows

def save_csv_preserve_structure(file_path, original_rows, new_values_dict):
    """
    Zapisuje CSV w oryginalnej kolejności i formacie.
    Nadpisuje tylko wartości.
    """
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')

        for key, old_val in original_rows:
            new_val = new_values_dict.get(key, old_val)
            writer.writerow([key, new_val])