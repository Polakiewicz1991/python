import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

i = 0
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
            time.sleep(1)
        # Pobierz wartość elementu
        value_element = driver.find_element(By.CSS_SELECTOR,
                                            'body div#background.switchStyle div#page div#fscontainer div#fselement div#datacontainer div#tablecontainer div.tablegroup div.commandcontainer div.tablerow div.tableElement div.valueContainer span.value')

        # Sprawdzanie, czy element istnieje, i wypisanie wartości
        if value_element:
            print("Wartość:", value_element.text.strip())
        else:
            print("Element nie został znaleziony.")


        try:
            # Wybieranie 6-tego div.tablerow w div.commandcontainer
            sixth_row = driver.find_element(By.CSS_SELECTOR, 'div.commandcontainer div.tablerow:nth-of-type(6)')

            # Możesz teraz pracować z 'sixth_row', np. odczytać tekst z elementu
            print("Zawartość 6-tego wiersza:", sixth_row.text)

        except Exception as e:
            print("Wystąpił błąd:", e)

except KeyboardInterrupt:
    # Obsługuje przerwanie programu (np. Ctrl+C)
    print("Zakończono pobieranie danych.")
    driver.quit()