import requests
from bs4 import BeautifulSoup

# Wysyłanie żądania HTTP do strony
url = 'https://192.168.1.130/actualSystemData/actualSystemData.html'
response = requests.get(url, verify=False)  # verify=False, aby wyłączyć weryfikację certyfikatu (jeśli dotyczy)

# Tworzenie obiektu BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


print(soup)
# Wyszukiwanie konkretnego elementu w HTML
value_element = soup.select_one('body div#background.switchStyle div#page div#fscontainer div#fselement div#datacontainer div#tablecontainer div.tablegroup div.commandcontainer div.tablerow div.tableElement div.valueContainer span.value')

# Sprawdzamy, czy element został znaleziony i wypisujemy jego tekst
if value_element:
    print("Wartość:", value_element.text.strip())
else:
    print("Element nie został znaleziony.")