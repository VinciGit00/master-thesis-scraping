# Web Scraping Evolution: From Classic to AI-Powered Approaches

This repository demonstrates the evolution of web scraping techniques through three different implementations: classic web scraping, AI-powered graph-based scraping, and modern SDK-based scraping. Each approach is tested against four popular websites to compare effectiveness, maintainability, and performance.

This project is part of a master thesis research on the evolution of web scraping techniques, focusing on how AI and modern tools are transforming the field. The implementations showcase:

1. **Traditional Approach**: Using BeautifulSoup4 for HTML parsing and manual data extraction
   - Direct HTML parsing with CSS selectors
   - Manual pattern recognition
   - Custom error handling
   - Regular maintenance required

2. **AI-Graph Approach**: Leveraging ScrapegraphAI's graph-based system with LLM capabilities
   - LLM-powered content understanding
   - Automatic pattern recognition
   - Smart error recovery
   - Graph-based execution flow
   - Self-adapting to site changes

3. **Modern SDK Approach**: Utilizing Scrapegraph's Python SDK for streamlined, production-ready scraping
   - Clean API interface
   - Built-in error handling
   - Type safety with Pydantic
   - Production-ready features
   - Minimal maintenance needed

Each implementation is tested against four diverse websites to evaluate:
- Scraping accuracy and data quality
- Code maintainability and complexity
- Performance metrics and resource usage
- Error handling capabilities and resilience
- Adaptation to site changes and updates
- Development time and effort
- Long-term maintenance costs

The project includes comprehensive benchmarking over 100 iterations for each approach, providing insights into:
- Average execution time per request
- Success rates and reliability
- Data quality and consistency
- Resource usage (CPU, memory, network)
- Maintainability costs and effort
- Error rates and recovery
- Adaptation to site changes

## Target Websites Selection

The four target websites were carefully selected to represent different challenges in web scraping:

1. **IKEA (E-commerce)**
   - Dynamic content loading
   - Complex product structures
   - Multiple data points per item
   - Regular layout updates

2. **Nature (Scientific Articles)**
   - Structured academic content
   - Multiple authors and metadata
   - Publication dates and citations
   - Complex article hierarchies

3. **Walmart (E-commerce)**
   - Large-scale product catalog
   - Dynamic pricing
   - Multiple product variations
   - Heavy JavaScript usage

4. **Wired (News Articles)**
   - Article content extraction
   - Author and date information
   - Related articles handling
   - Multimedia content

## Research Goals

This research aims to:
1. Compare traditional and AI-powered scraping approaches
2. Evaluate the effectiveness of LLM in web scraping
3. Measure the impact on development and maintenance
4. Assess scalability and reliability
5. Analyze cost-effectiveness
6. Provide guidelines for choosing appropriate scraping methods

## Repository Structure
