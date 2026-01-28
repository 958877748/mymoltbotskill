---
name: duckduckgo_search
description: Search the web using DuckDuckGo without requiring an API key.
---

# DuckDuckGo Search

Perform web searches using DuckDuckGo's search engine without requiring an API key.

## Usage

```bash
python ddg_search.py "search query"                    # Search with default 5 results
python ddg_search.py "search query" -n 10             # Search with 10 results
```

## Features

- No API key required
- Returns search results with title, link, and summary
- Configurable number of results
- Clean, readable output format

## Dependencies

- ddgs (DuckDuckGo Search Python library)

## When to Use

- When you need to search the web without an API key
- For quick fact-checking or information gathering
- When privacy is a concern (DuckDuckGo doesn't track users)
- As an alternative to other search APIs that require authentication