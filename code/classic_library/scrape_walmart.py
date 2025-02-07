import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_walmart():
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
    
    return products

def main():
    total_time = 0
    iterations = 100
    
    for i in range(iterations):
        start_time = time.time()
        products = scrape_walmart()
        end_time = time.time()
        total_time += (end_time - start_time)
        
        if i == 0:  # Print results only for the first iteration
            print(json.dumps(products, indent=2))
    
    avg_time = total_time / iterations
    print(f"\nAverage execution time over {iterations} iterations: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main()