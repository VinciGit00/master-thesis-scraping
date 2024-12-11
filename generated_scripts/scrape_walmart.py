import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "https://www.walmart.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for product in soup.find_all('div', class_='card-wrapper'):
        name = product.find('p', class_='b')
        price = product.find('span', class_='cart-total')
        image = product.find('img', class_='w-100')

        if name and price and image:
            products.append({
                'name': name.get_text(strip=True),
                'price': price.get_text(strip=True),
                'image': image['src']
            })

    print(json.dumps(products, indent=2))

if __name__ == "__main__":
    main()