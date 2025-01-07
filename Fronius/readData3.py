import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

i = 0
current_file_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Funkcja do zapisywania danych do pliku CSV
def save_to_csv(data):
    file_path = f"dane_{current_file_time}.csv"
    try:
        # Sprawdzamy, czy plik istnieje
        file_exists = False
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            pass

        # Jeśli plik istnieje, dodajemy dane
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                # Jeśli plik nie istnieje, zapisujemy nagłówki
                writer.writerow(['Czas Odczytu', 'Current [A]', 'Flow [l/min]', 'Temp [°C]'])

            # Zapisujemy dane do pliku
            writer.writerow(data)

        print(f"Dane zapisane do {file_path}")
    except Exception as e:
        print(f"Błąd podczas zapisywania do CSV: {e}")


# Ustawienie WebDrivera
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Otwórz stronę
url = 'https://192.168.1.130/actualSystemData/actualSystemData.html'
driver.get(url)

try:
    while True:
        if i == 0:
            time.sleep(15)
            i += 1
        else:
            time.sleep(0.2)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # try:
        #     # Pobieramy wszystkie wiersze tablerow
        #     rows = driver.find_elements(By.CSS_SELECTOR, 'div.commandcontainer div.tablerow')
        #
        #
        #     # Iterujemy przez każdy wiersz
        #     for index, row in enumerate(rows):
        #         try:
        #             # Pobierz wartość ze span.value w tym wierszu
        #             value_element = row.find_element(By.CSS_SELECTOR, 'div.tableElement div.valueContainer span.value')
        #             print(f"Wartość wiersza {index + 1}: {value_element.text.strip()}")
        #             if index == 0:
        #                 current = value_element.text.strip()
        #                 print(f"Natężenie prądu: {current} [A]")
        #
        #             if index == 18:
        #                 flow = value_element.text.strip()
        #                 print(f"Przepływ cieczy: {flow} [l/min]")
        #
        #             if index == 19:
        #                 temp = value_element.text.strip()
        #                 print(f"Temperatura cieczy: {temp} [°C]")
        #
        #         except:
        #             print(f"Wartość wiersza {index + 1} jest pusta lub brak elementu.")
        #
        #     save_to_csv([current_time, current, flow, temp])
        #
        # except Exception as e:
        #     print("Wystąpił błąd:", e)

        try:
            # Znajdź wszystkie elementy valueContainer span.value
            value_elements = driver.find_elements(By.CSS_SELECTOR, 'div.valueContainer span.value')

            # Wyciągnij tekst z każdego elementu
            values = [element.text for element in value_elements]

            # Wyświetl wyniki
            print("Wyciągnięte wartości:")
            for index,value in enumerate(values):
                print(f"Wartość wiersza {index + 1}: ",value)
                if index == 3:
                    current = value
                    print(f"Natężenie prądu: {current} [A]")
                elif index == 4:
                    voltage = value
                    print(f"Napięcie prądu: {voltage} [V]")
                elif index == 6:
                    weldingTime = value
                    print(f"Czas spawania: {weldingTime} [s]")
                elif index == 65:
                    flow = value
                    print(f"Przepływ cieczy: {flow} [l/min]")

                elif index == 69:
                    temp = value
                    print(f"Temperatura cieczy: {temp} [°C]")

            save_to_csv([current_time, weldingTime, current, voltage, flow, temp])

        except Exception as e:
            print("Wystąpił błąd:", e)

except KeyboardInterrupt:
    # Obsługuje przerwanie programu (np. Ctrl+C)
    print("Zakończono pobieranie danych.")
    driver.quit()

