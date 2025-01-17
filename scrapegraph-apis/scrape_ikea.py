from typing import List, Optional
from pydantic import BaseModel, Field
from scrapegraph_py import Client
import os
from dotenv import load_dotenv

load_dotenv()

# ************************************************
# Define the output schema
# ************************************************

class Product(BaseModel):
    name: str = Field(description="The name of the product")
    price: Optional[float] = Field(description="The price of the product")
    image_url: str = Field(description="The URL of the product image")

class Products(BaseModel):
    products: List[Product]

def scrape_ikea():
    # Initialize the client
    sgai_client = Client(api_key=os.getenv("SGAI_API_KEY"))

    # SmartScraper request with output schema
    response = sgai_client.smartscraper(
        website_url="https://www.ikea.com",
        user_prompt="Extract all products with their names, prices and image URLs",
        output_schema=Products,
    )

    sgai_client.close()
    return response

if __name__ == "__main__":
    result = scrape_ikea()
    print(f"Request ID: {result['request_id']}")
    print(f"Result: {result['result']}") 