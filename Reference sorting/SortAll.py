import pandas as pd
from pathlib import Path


def sort_and_complete(template_path, target_path, sep=";"):
    template = pd.read_csv(template_path, sep=sep, engine="python", header=None)
    target = pd.read_csv(target_path, sep=sep, engine="python", header=None)
    print("template:\n",template)
    key_col = 0

    template_keys = template.iloc[:, key_col]
    target_keys = target.iloc[:, key_col]
    print("template_keys:\n",template_keys)
    # brakujące wiersze
    missing = template[~template_keys.isin(target_keys)]

    # połączenie
    combined = pd.concat([target, missing], ignore_index=True)

    # mapa kolejności
    order_map = {k: i for i, k in enumerate(template_keys)}
    combined["__order"] = combined.iloc[:, key_col].map(order_map)

    # sortowanie
    combined = combined.sort_values("__order")
    combined = combined.drop(columns="__order")

    # nadpisanie pliku
    combined.to_csv(target_path, sep=sep, index=False, header=False)

    print(f"✔ Zrobiono: {target_path.name}")


# 🔻 ŚCIEŻKI
folder = Path(r"E:\PP\22_0018_0000 - Stanowisko spawalnicze 2\Recepty\2026.02.19 — nowe")
template_file = folder / "NEW2.RefTable.CSV"


# 🔻 Przetwarzanie wszystkich CSV
for csv_file in folder.glob("*.CSV"):

    if csv_file.name == template_file.name:
        continue  # pomiń wzorzec

    sort_and_complete(template_file, csv_file)

print("\n✅ GOTOWE – wszystkie pliki posortowane i uzupełnione")
