import requests
from bs4 import Beauimport requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a request to the website
url = "https://www.ebay.com/b/Electronics/bn_7000259124"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the information you want to scrape
product_names = [item.text for item in soup.find_all(class_='s-item__title')]
prices = [item.text for item in soup.find_all(class_='s-item__price')]

# Create a DataFrame
df = pd.DataFrame({'Product Name': product_names, 'Price': prices})

# Display the first few rows of the DataFrame
print(df.head())
tifulSoup
import pandas as pd

# Send a request to the website
url = "https://www.ebay.com/b/Electronics/bn_7000259124"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the information you want to scrape
product_names = [item.text for item in soup.find_all(class_='s-item__title')]
prices = [item.text for item in soup.find_all(class_='s-item__price')]

# Create a DataFrame
df = pd.DataFrame({'Product Name': product_names, 'Price': prices})

# Display the first few rows of the DataFrame
print(df.head())
