import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com/news"
response = requests.get(url)

# Create a Beautiful Soup object
soup = BeautifulSoup(response.text, "html.parser")

# Find all the headline elements
headlines = soup.find_all("h1", class_="headline")

# Extract the text from the headlines
for headline in headlines:
    print(headline.text.strip())
