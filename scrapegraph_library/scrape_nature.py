import json
import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import time

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
            prompt="Extract all articles with their titles, authors and publication dates",
            source="https://www.nature.com",
            config=graph_config,
            schema=Articles
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