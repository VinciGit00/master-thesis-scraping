import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_ikea():
    url = "https://www.ikea.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    for item in soup.find_all('a', class_='item image-overlay__holder svelte-ucs4w0'):
        name = item.find('p', class_='svelte-ucs4w0').text
        image = item.find('img')['src']
        price = None
        products.append({'name': name, 'price': price, 'image': image})
    
    return products

def main():
    total_time = 0
    iterations = 100
    
    for i in range(iterations):
        start_time = time.time()
        products = scrape_ikea()
        end_time = time.time()
        total_time += (end_time - start_time)
        
        if i == 0:  # Print results only for the first iteration
            print(json.dumps(products, indent=2))
    
    avg_time = total_time / iterations
    print(f"\nAverage execution time over {iterations} iterations: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main()