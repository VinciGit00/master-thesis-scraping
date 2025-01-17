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
    authors: List[str] = Field(description="List of article authors")
    publication_date: str = Field(description="The publication date of the article")

class Articles(BaseModel):
    articles: List[Article]

def scrape_nature():
    # Initialize the client
    sgai_client = Client(api_key=os.getenv("SGAI_API_KEY"))

    # SmartScraper request with output schema
    response = sgai_client.smartscraper(
        website_url="https://www.nature.com",
        user_prompt="Extract all articles with their titles, authors and publication dates",
        output_schema=Articles,
    )

    sgai_client.close()
    return response

if __name__ == "__main__":
    result = scrape_nature()
    print(f"Request ID: {result['request_id']}")
    print(f"Result: {result['result']}") 