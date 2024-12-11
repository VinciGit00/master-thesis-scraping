import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "https://www.ikea.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    for item in soup.find_all('a', class_='item image-overlay__holder svelte-ucs4w0'):
        name = item.find('p', class_='svelte-ucs4w0').text
        image = item.find('img')['src']
        # Assuming price is not available in the provided HTML, setting it as None
        price = None
        products.append({'name': name, 'price': price, 'image': image})
    
    print(json.dumps(products, indent=2))

if __name__ == "__main__":
    main()