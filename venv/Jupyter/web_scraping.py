import sys
#print(sys.executable)
#print(sys.version)
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com/news'

# Make an HTTP request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# Find elements containing the titles - adjust the selector as needed
titles = soup.find_all('h1', class_='title')

# Print each title
for title in titles:
    print(title.text.strip())

