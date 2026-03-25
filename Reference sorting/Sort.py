import pandas as pd
from pathlib import Path


def sort_and_complete(template_path, target_path, sep=";"):
    template_path = Path(template_path)
    target_path = Path(target_path)

    template = pd.read_csv(template_path, sep=sep, engine="python", header=None)
    target = pd.read_csv(target_path, sep=sep, engine="python", header=None)

    key_col = 0

    template_keys = template.iloc[:, key_col]
    target_keys = target.iloc[:, key_col]

    # brakujące wiersze z wzorca
    missing = template[~template_keys.isin(target_keys)]

    # połączenie danych
    combined = pd.concat([target, missing], ignore_index=True)

    # mapa kolejności
    order_map = {k: i for i, k in enumerate(template_keys)}
    combined["__order"] = combined.iloc[:, key_col].map(order_map)

    # sortowanie
    combined = combined.sort_values("__order")
    combined = combined.drop(columns="__order")

    # 🔴 NADPISANIE ORYGINALNEGO PLIKU
    combined.to_csv(target_path, sep=sep, index=False, header=False)

    print(f"✔ Plik został nadpisany: {target_path}")


if __name__ == "__main__":
    template_file = r"E:\PP\22_0018_0000 - Stanowisko spawalnicze 2\Recepty\2026.02.19 — nowe\NEW2.RefTable.CSV"
    target_file = r"E:\PP\22_0018_0000 - Stanowisko spawalnicze 2\Recepty\2026.02.19 — nowe\N16X1004X504X106.RefTable.CSV"

    sort_and_complete(template_file, target_file)
