# Get the webpage
# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests

# Get a soup from a URL
url = 'https://www.hshv.org/petsoftheweek/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# Get info from one tag
# Get first tag of a certain type from the soup
tag = soup.find('a', class_='pt-cv-none cvplbd')
# Get info from tag
info = tag.text

# Print the info
print(info)
