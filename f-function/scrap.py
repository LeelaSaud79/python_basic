'''Web scraping is the process of extracting datafrom various websites and parsing it.
In other words, it's a technique to extractunstructured data and store that data either
in a local file or in a database Beautiful Soup can select HTML
elements using either XPath or CSS selectors'''

import requests
from bs4 import BeautifulSoup
url = "https://www.facebook.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))


