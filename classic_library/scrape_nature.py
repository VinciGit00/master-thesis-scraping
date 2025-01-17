import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_nature():
    url = "https://www.nature.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for article in soup.find_all('article', class_='c-card'):
        title_tag = article.find('h3', class_='c-card__title')
        title = title_tag.get_text(strip=True) if title_tag else None

        author_tags = article.find_all('li', itemprop='creator')
        authors = [author.get_text(strip=True) for author in author_tags]

        date_tag = article.find('time', class_='c-meta__item')
        date = date_tag['datetime'] if date_tag else None

        if title and authors and date:
            articles.append({
                'title': title,
                'authors': authors,
                'date': date
            })
    
    return articles

def main():
    total_time = 0
    iterations = 100
    
    for i in range(iterations):
        start_time = time.time()
        articles = scrape_nature()
        end_time = time.time()
        total_time += (end_time - start_time)
        
        if i == 0:  # Print results only for the first iteration
            print(json.dumps(articles, indent=2))
    
    avg_time = total_time / iterations
    print(f"\nAverage execution time over {iterations} iterations: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main()