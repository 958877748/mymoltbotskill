"""
DuckDuckGo Search Skill - Package Init

This module provides functions to search the web using DuckDuckGo
without requiring an API key.
"""

from .ddg_search import skill_ddg_search, search_ddg, format_results

__all__ = [
    'skill_ddg_search',
    'search_ddg',
    'format_results'
]

__version__ = "1.0.0"
__author__ = "Assistant"