# Moltbot Skills Configuration

This repository contains two custom skills for Moltbot:

## 1. DuckDuckGo Search Skill

**Directory:** `duckduckgo_search/`

**Description:** Allows Moltbot to perform web searches using DuckDuckGo without requiring an API key.

**Files:**
- `SKILL.md` - Skill documentation and metadata
- `ddg_search.py` - Main search functionality
- `__init__.py` - Module initialization

**Installation:** Copy the entire `duckduckgo_search` directory to your Moltbot skills directory.

## 2. Resend Mail Skill

**Directory:** `resend_mail/`

**Description:** Enables Moltbot to send emails using the Resend API service.

**Files:**
- `SKILL.md` - Skill documentation and metadata
- `send_mail.py` - Main email sending functionality
- `__init__.py` - Module initialization

**Installation:** Copy the entire `resend_mail` directory to your Moltbot skills directory. Requires Resend API key configuration.

## Installation Instructions

To install these skills in your Moltbot instance:

1. Clone this repository
2. Copy the skill directories to your Moltbot skills folder
3. Ensure dependencies are installed (for resend: `pip install resend`)
4. Restart Moltbot to recognize the new skills

## Requirements

- Python 3.7+
- For resend_mail: `resend` Python package
- For duckduckgo_search: `requests` Python package (usually already installed)