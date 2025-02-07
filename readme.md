# Master Thesis: Evolution of Web Scraping Techniques

This repository contains the research, implementation, and documentation for my master thesis on the evolution of web scraping techniques, comparing traditional approaches with modern AI-powered solutions.

## 📁 Repository Structure

The repository is organized into two main sections:

### `/code`
Contains all the implementation code for the web scraping experiments:
- `classic_library/`: Traditional web scraping implementations using BeautifulSoup4
- `scrapegraph_library/`: AI-powered graph-based scraping implementations
- `scrapegraph-apis/`: Modern SDK-based scraping implementations
- `generate_scraper.py`: Utility script for scraper generation
- `scrapegraph_scraping.py`: Main scraping execution script
- `scraping_results.json`: Collected experimental results

### `/latex`
Contains the thesis document and related materials:
- `chapters/`: Individual thesis chapters
- `images/`: Figures and diagrams
- `Assets/`: Additional resources
- `main.tex`: Main LaTeX document
- `bibliography.bib`: References and citations
- `unibg.cls`: University document class

## 🔬 Research Overview

This thesis investigates the evolution of web scraping techniques through three distinct approaches:

1. **Traditional Web Scraping**
   - Implementation: BeautifulSoup4
   - Features: Manual HTML parsing, CSS selectors, custom error handling
   - Location: `code/classic_library/`

2. **AI-Powered Graph-Based Scraping**
   - Implementation: ScrapegraphAI with LLM capabilities
   - Features: Automatic pattern recognition, smart error recovery, graph-based execution
   - Location: `code/scrapegraph_library/`

3. **Modern SDK-Based Scraping**
   - Implementation: Scrapegraph Python SDK
   - Features: Clean API interface, built-in error handling, type safety
   - Location: `code/scrapegraph-apis/`

## 🎯 Target Websites

The research evaluates each approach against four diverse websites:

1. **IKEA** (E-commerce)
   - Dynamic content loading
   - Complex product structures
   - Regular layout updates

2. **Nature** (Scientific Articles)
   - Structured academic content
   - Multiple authors and metadata
   - Publication data and citations

3. **Walmart** (E-commerce)
   - Large-scale product catalog
   - Dynamic pricing
   - Heavy JavaScript usage

4. **Wired** (News Articles)
   - Article content extraction
   - Author and date information
   - Multimedia content handling

## 📊 Evaluation Metrics

The research compares the approaches based on:
- Scraping accuracy and data quality
- Code maintainability and complexity
- Performance metrics and resource usage
- Error handling capabilities
- Adaptation to site changes
- Development time and effort
- Long-term maintenance costs

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/master-thesis-scraping.git
cd master-thesis-scraping
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run experiments:
```bash
python code/scrapegraph_scraping.py
```

## 📖 Thesis Document

The thesis document can be compiled using:
```bash
cd latex
make
```

The compiled PDF will be available in the `latex` directory.

## 📝 License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.

## 📚 Citation

If you use this work in your research, please cite using the information provided in [CITATION.cff](CITATION.cff).

## 👥 Contact

For questions or feedback about this research, please open an issue or contact the author directly.

---
This research is conducted as part of a Master's Thesis at the University of Bergamo.
