import requests
from bs4 import BeautifulSoup 
from unidecode import unidecode

# Makes the HTTP request to the website and returns the cities of pernambuco 
url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Pernambuco_por_popula%C3%A7%C3%A3o'
response = requests.get(url)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable sortable'})

# Extract the cities from the table
cities = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    city_name = columns[1].text.strip()
    city_name = unidecode(city_name) # remove accents
    cities.append(city_name)


