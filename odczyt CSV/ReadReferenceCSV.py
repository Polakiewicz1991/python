import csv

# Ścieżka do pliku CSV
file_path = 'nazwa_pliku.csv'

# Słownik do przechowywania danych
data = {}

# Otwieranie pliku CSV i odczytywanie danych
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        # Ignorowanie pustych wierszy
        if len(row) == 0:
            continue

        # Podział wiersza na klucz i wartość
        key_value = row[0].split('\t')
        key = key_value[0].strip()
        value = key_value[1].strip()

        # Dodanie danych do słownika
        data[key] = value

# Wyświetlenie odczytanych danych
for key, value in data.items():
    print(f"{key}: {value}")