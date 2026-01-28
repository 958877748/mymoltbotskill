#!/usr/bin/env python3
"""
DuckDuckGo Search Skill
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
        return results
    except Exception as e:
        print(f"Error performing search: {e}")
        return []


def format_results(results, query):
    """
    Format search results for display
    
    Args:
        results (list): Raw search results
        query (str): Original search query
    
    Returns:
        str: Formatted results string
    """
    if not results:
        return f"No results found for '{query}'"
    
    formatted = f"🔍 DuckDuckGo Search Results for '{query}':\n"
    formatted += "=" * 50 + "\n"
    
    for i, result in enumerate(results, 1):
        formatted += f"{i}. {result.get('title', 'No title')}\n"
        formatted += f"   Link: {result.get('href', 'No link')}\n"
        formatted += f"   Summary: {result.get('body', 'No summary')}\n\n"
    
    return formatted


def skill_ddg_search(query, num_results=5):
    """
    Main skill function to perform DuckDuckGo search
    
    Args:
        query (str): Search query
        num_results (int): Number of results to return
    
    Returns:
        str: Formatted search results
    """
    results = search_ddg(query, num_results)
    return format_results(results, query)


def main():
    parser = argparse.ArgumentParser(description='DuckDuckGo Search Skill')
    parser.add_argument('query', nargs='+', help='Search query terms')
    parser.add_argument('-n', '--num-results', type=int, default=5, 
                        help='Number of results to return (default: 5)')
    
    args = parser.parse_args()
    query = ' '.join(args.query)
    
    results = skill_ddg_search(query, args.num_results)
    print(results)


if __name__ == "__main__":
    main()