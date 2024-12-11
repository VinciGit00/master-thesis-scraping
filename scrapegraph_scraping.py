import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

urls = {
    "https://www.wired.com": "Extract all the articles",
    "https://www.walmart.com": "Extract all the products with name, price, and image",
    "https://www.ikea.com": "Extract all the products with name, price, and image",
    "https://www.nature.com": "Extract all the articles with title, author, and date",
}

# Iterate through both URL and prompt using .items()
for url, prompt in urls.items():
    print(f"Processing URL: {url}")
    print(f"Prompt: {prompt}")

    graph_config = {
        "llm": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "openai/gpt-4o",
        },
        "verbose": True,
        "headless": False,
    }

    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,  # Use the prompt from the dictionary
        source=url,    # Use the URL from the dictionary
        config=graph_config
    )

    result = smart_scraper_graph.run()
    print(json.dumps(result, indent=4))

    graph_exec_info = smart_scraper_graph.get_execution_info()
    print(prettify_exec_info(graph_exec_info))
    print("-" * 80)  # Add a separator between iterations