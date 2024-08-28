import requests
from bs4 import BeautifulSoup

#  URL of the web page where data will be collected
url = 'https://www.example.com'

# GET request is made to retrieve the web page
response = requests.get(url)

#  The content of the web page is parse with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all headings (h1 tags)
basliklar = soup.find_all('h1')

#  Print each title on the screen
for baslik in basliklar:
    print(baslik.text)