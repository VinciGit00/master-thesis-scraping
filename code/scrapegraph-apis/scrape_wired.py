from typing import List
from pydantic import BaseModel, Field
from scrapegraph_py import Client
import os
from dotenv import load_dotenv

load_dotenv()

# ************************************************
# Define the output schema
# ************************************************

class Article(BaseModel):
    title: str = Field(description="The title of the article")
    url: str = Field(description="The URL of the article")

class Articles(BaseModel):
    articles: List[Article]

def scrape_wired():
    # Initialize the client
    sgai_client = Client(api_key=os.getenv("SGAI_API_KEY"))

    # SmartScraper request with output schema
    response = sgai_client.smartscraper(
        website_url="https://www.wired.com",
        user_prompt="Extract all articles with their titles and URLs",
        output_schema=Articles,
    )

    sgai_client.close()
    return response

if __name__ == "__main__":
    result = scrape_wired()
    print(f"Request ID: {result['request_id']}")
    print(f"Result: {result['result']}") 