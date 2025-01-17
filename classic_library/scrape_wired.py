import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_wired():
    url = "https://www.wired.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    data = json.loads(script_tag.string)
    articles = data['itemListElement']
    return [{'name': article['name'], 'url': article['url']} for article in articles]

def main():
    total_time = 0
    iterations = 100
    
    for i in range(iterations):
        start_time = time.time()
        articles = scrape_wired()
        end_time = time.time()
        total_time += (end_time - start_time)
        
        if i == 0:  # Print results only for the first iteration
            print(json.dumps(articles, indent=2))
    
    avg_time = total_time / iterations
    print(f"\nAverage execution time over {iterations} iterations: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main()