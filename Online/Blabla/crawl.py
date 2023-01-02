import requests
from bs4 import BeautifulSoup

# Set the URL you want to crawl
url = "https://tiki.vn/dien-thoai-di-dong/c1795?src=c.1795.hamburger_menu_fly_out_banner"

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the product elements on the page
products = soup.find_all("div", class_="product-item")

# Loop through the products
for product in products:
    # Extract the product name and price
    name = product.find("p", class_="title").text.strip()
    price = product.find("span", class_="final-price").text.strip()

    # Print the product name and price
    print(name, price)
