import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "https://www.wired.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', type='application/ld+json')
    data = json.loads(script_tag.string)
    articles = data['itemListElement']
    articles_list = [{'name': article['name'], 'url': article['url']} for article in articles]
    print(json.dumps(articles_list, indent=2))

if __name__ == "__main__":
    main()