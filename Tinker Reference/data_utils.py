import csv
import os
import re

def read_csv_to_nested_dict(file_path):
    data = {}
    prefix = "GVL_Reference.MAP."
    array_data = {}

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) != 2:
                continue

            full_key = row[0].strip()
            value = row[1].strip()

            if full_key.startswith(prefix):
                full_key = full_key[len(prefix):]

            match = re.match(r"(.*?)\[(\d+),\s*(\d+)\]", full_key)
            if match:
                var_name = match.group(1)
                row_idx = int(match.group(2)) - 1
                col_idx = int(match.group(3))
                try:
                    value = float(value) if '.' in value else int(value)
                except ValueError:
                    pass
                if var_name not in array_data:
                    array_data[var_name] = []
                array_data[var_name].append((row_idx, col_idx, value))
                continue

            # Try numeric conversion
            if value.replace('.', '', 1).isdigit():
                value = float(value) if '.' in value else int(value)

            # Handle nested structures
            parts = full_key.split('.')
            if parts[0].startswith("st"):
                current = data
                for part in parts[:-1]:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                current[parts[-1]] = value
            else:
                data[parts[-1]] = value

    # Convert collected 2D arrays
    for name, entries in array_data.items():
        max_row = max(i for i, _, _ in entries)
        max_col = max(j for _, j, _ in entries)
        matrix = [[0 for _ in range(max_col + 1)] for _ in range(max_row + 1)]
        for i, j, val in entries:
            matrix[i][j] = val
        data[name] = matrix

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

# def write_dict_to_csv(data, file_path, prefix="GVL_Reference.MAP."):
    # def flatten_dict(prefix_path, value, rows):
    #     if isinstance(value, dict):
    #         for k, v in value.items():
    #             flatten_dict(f"{prefix_path}{k}.", v, rows)
    #     elif isinstance(value, list):
    #         if all(isinstance(row, list) for row in value):
    #             for i, row in enumerate(value):
    #                 for j, cell in enumerate(row):
    #                     rows.append([f"{prefix_path[:-1]}[{i+1}, {j}]", cell])
    #         else:
    #             for i, cell in enumerate(value):
    #                 rows.append([f"{prefix_path[:-1]}[{i}]", cell])
    #     else:
    #         rows.append([prefix_path[:-1], value])
    #
    # rows = []
    # for key, value in data.items():
    #     flatten_dict(prefix + key + ".", value, rows)
    #
    # # Zapis do pliku CSV
    # with open(file_path, "w", encoding="utf-8", newline="") as f:
    #     writer = csv.writer(f, delimiter=";")
    #     writer.writerows(rows)
def write_dict_to_csv(data, file_path):
    """
    Zapisuje dane w formacie:
    GVL_Reference.MAP.iRobotPlasmaSteps[1, 0];3
    """
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
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