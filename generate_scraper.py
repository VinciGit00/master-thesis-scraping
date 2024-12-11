urls = {
    "https://www.wired.com": "Extract all the articles",
    "https://www.walmart.com": "Extract all the products with name, price, and image",
    "https://www.ikea.com": "Extract all the products with name, price, and image",
    "https://www.nature.com": "Extract all the articles with title, author, and date",
}

""" 
Basic example of scraping pipeline using SmartScraper
"""
import os
import json
from dotenv import load_dotenv
from scrapegraphai.graphs import ScriptCreatorGraph
from scrapegraphai.utils import prettify_exec_info
from pathlib import Path

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "model": "openai/gpt-4o",
    },
    "library": "beautifulsoup",
    "verbose": True,
    "headless": False,
}

# ************************************************
# Iterate through URLs and scrape each one
# ************************************************

all_results = {}

# Create a directory to store the scripts
scripts_dir = Path("generated_scripts")
scripts_dir.mkdir(exist_ok=True)

for url, prompt in urls.items():
    print(f"\nProcessing {url}...")
    try:
        smart_scraper_graph = ScriptCreatorGraph(
            prompt=prompt,
            source=url,
            config=graph_config
        )

        result = smart_scraper_graph.run()
        all_results[url] = result

        # Save the generated script
        domain = url.split("//")[1].split(".")[1]  # Extract domain name (e.g., walmart from www.walmart.com)
        script_path = scripts_dir / f"scrape_{domain}.py"
        
        # Extract the Python code from the result
        if isinstance(result, dict) and 'python_script' in result:
            script_content = result['python_script']
        elif isinstance(result, str):
            # Try to extract Python code from markdown format
            if "```python" in result:
                script_content = result.split("```python")[1].split("```")[0].strip()
            else:
                script_content = result
        else:
            print(f"Warning: Could not extract Python script for {url}")
            continue
        
        # Add imports if they're not present
        required_imports = """import requests
from bs4 import BeautifulSoup
import json
"""
        if "import" not in script_content:
            script_content = required_imports + "\n" + script_content

        # Add main block if it's not present
        if "__main__" not in script_content:
            script_content += "\n\nif __name__ == '__main__':\n    main()"
        
        with open(script_path, "w") as f:
            f.write(script_content)
        print(f"Saved script to: {script_path}")

        # Print individual results and execution info
        print(f"\nResults for {url}:")
        print(json.dumps(result, indent=4))
        
        graph_exec_info = smart_scraper_graph.get_execution_info()
        print("\nExecution Info:")
        print(prettify_exec_info(graph_exec_info))
        
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        all_results[url] = {"error": str(e)}

# ************************************************
# Save all results to a file
# ************************************************

output_file = "scraping_results.json"
with open(output_file, "w") as f:
    json.dump(all_results, f, indent=4)

print(f"\nAll results have been saved to {output_file}")
print(f"Generated scripts have been saved in the '{scripts_dir}' directory")