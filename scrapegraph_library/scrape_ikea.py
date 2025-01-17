import json
import os
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import time

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

# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4-mini",
    },
    "verbose": True,
    "headless": False,
}

def main():
    total_time = 0
    iterations = 100
    
    for i in range(iterations):
        start_time = time.time()
        
        smart_scraper_graph = SmartScraperGraph(
            prompt="Extract all products with their names, prices and image URLs",
            source="https://www.ikea.com",
            config=graph_config,
            schema=Products
        )
        
        result = smart_scraper_graph.run()
        end_time = time.time()
        total_time += (end_time - start_time)
        
        if i == 0:  # Print results only for the first iteration
            print(json.dumps(result, indent=4))
            graph_exec_info = smart_scraper_graph.get_execution_info()
            print(prettify_exec_info(graph_exec_info))
    
    avg_time = total_time / iterations
    print(f"\nAverage execution time over {iterations} iterations: {avg_time:.2f} seconds")

if __name__ == "__main__":
    main() 