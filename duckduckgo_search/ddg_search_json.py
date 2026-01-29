#!/usr/bin/env python3
"""
DuckDuckGo Search Skill - JSON output version
Uses the ddgs library to perform searches without requiring an API key
"""

from ddgs import DDGS
import argparse
import sys
import json


def search_ddg(query, num_results=5):
    """
    Perform a DuckDuckGo search
    
    Args:
        query (str): Search query
        num_results (int): Number of results to return (default 5)
    
    Returns:
        list: Search results
    """
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=num_results)
        # Convert to standard format
        formatted_results = []
        for result in results:
            formatted_results.append({
                "title": result.get('title', ''),
                "link": result.get('href', ''),
                "summary": result.get('body', '')
            })
        return formatted_results
    except Exception as e:
        print(f"Error performing search: {e}", file=sys.stderr)
        return []


def main():
    parser = argparse.ArgumentParser(description='DuckDuckGo Search Skill (JSON output)')
    parser.add_argument('query', nargs='+', help='Search query terms')
    parser.add_argument('-n', '--num-results', type=int, default=5, 
                        help='Number of results to return (default: 5)')
    
    args = parser.parse_args()
    query = ' '.join(args.query)
    
    results = search_ddg(query, args.num_results)
    # Output JSON to stdout
    print(json.dumps(results, ensure_ascii=False))


if __name__ == "__main__":
    main()