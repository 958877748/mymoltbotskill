# Clawdbot Adapter for Moltbot Skills

This document describes how to adapt Moltbot skills for use with Clawdbot.

## Overview

The skills in this repository were originally designed for Moltbot, which uses Python scripts. To use these skills with Clawdbot, JavaScript adapters are needed to interface with the Python scripts.

## Required Adaptations

### 1. DuckDuckGo Search Skill

The original `duckduckgo_search/ddg_search.py` script can be called from Clawdbot using a JavaScript adapter:

```javascript
const { execSync } = require('child_process');
const path = require('path');

class DuckDuckGoSearchSkill {
  constructor() {
    this.name = 'duckduckgo_search';
    this.description = 'Search the web using DuckDuckGo without requiring an API key.';
  }

  async search(query, num_results = 5) {
    try {
      if (!query || typeof query !== 'string') {
        throw new Error('Query is required and must be a string');
      }

      if (typeof num_results !== 'number' || num_results <= 0) {
        num_results = 5;
      }

      const scriptPath = path.join(process.cwd(), 'mymoltbotskill/duckduckgo_search/ddg_search.py');
      const command = `python3 ${scriptPath} "${query.replace(/"/g, '')}" -n ${num_results}`;
      
      const result = execSync(command, { encoding: 'utf-8', timeout: 15000 });
      return result;
    } catch (error) {
      console.error(`DuckDuckGo search error: ${error.message}`);
      return `Error performing DuckDuckGo search: ${error.message}`;
    }
  }
}

module.exports = DuckDuckGoSearchSkill;
```

### 2. Resend Mail Skill

The original `resend_mail/send_mail.py` script can be called from Clawdbot using a JavaScript adapter:

```javascript
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

class ResendMailSkill {
  constructor() {
    this.name = 'resend_mail';
    this.description = 'Send emails using the Resend API service.';
  }

  async send_email(to_email, subject, body, from_email = "onboarding@resend.dev") {
    try {
      if (!to_email || !subject || !body) {
        throw new Error('to_email, subject, and body are required');
      }

      // Validate inputs
      if (typeof to_email !== 'string' || !to_email.includes('@')) {
        throw new Error('to_email must be a valid email address');
      }

      if (typeof subject !== 'string') {
        throw new Error('subject must be a string');
      }

      if (typeof body !== 'string') {
        throw new Error('body must be a string');
      }

      if (typeof from_email !== 'string' || !from_email.includes('@')) {
        throw new Error('from_email must be a valid email address');
      }

      // Create a temporary file to handle the email body with proper formatting
      const tempBodyFile = `/tmp/email_body_${Date.now()}_${Math.floor(Math.random() * 10000)}.txt`;
      
      // Write the body content to a temporary file to preserve all formatting
      fs.writeFileSync(tempBodyFile, body);

      try {
        // Read the content back to ensure it's properly formatted
        const bodyContent = fs.readFileSync(tempBodyFile, 'utf8');
        
        // Execute the Python script from the mymoltbotskill directory
        const scriptPath = path.join(process.cwd(), 'mymoltbotskill/resend_mail/send_mail.py');
        
        // Properly escape special characters for the shell command
        const escapedTo = to_email.replace(/'/g, "'\\''");
        const escapedSubject = subject.replace(/'/g, "'\\''");
        const escapedFrom = from_email.replace(/'/g, "'\\''");
        
        const command = `python3 ${scriptPath} --to '${escapedTo}' --subject '${escapedSubject}' --body '${bodyContent.replace(/'/g, "'\\''")}' --from-email '${escapedFrom}'`;
        
        const result = execSync(command, { encoding: 'utf-8', timeout: 15000 });
        return result;
      } finally {
        // Always clean up the temporary file
        if (fs.existsSync(tempBodyFile)) {
          fs.unlinkSync(tempBodyFile);
        }
      }
    } catch (error) {
      console.error(`Resend mail error: ${error.message}`);
      return `Error sending email: ${error.message}`;
    }
  }
}

module.exports = ResendMailSkill;
```

## Installation for Clawdbot

To install these skills in Clawdbot:

1. Install the required Python dependencies:
   ```bash
   python3 -m pip install --break-system-packages ddgs resend
   ```

2. Create the appropriate directory structure in Clawdbot's skills directory:
   ```
   /path/to/clawdbot/skills/duckduckgo_search/
   /path/to/clawdbot/skills/resend_mail/
   ```

3. Place the JavaScript adapters in the respective directories with `index.js` filenames.

4. Create corresponding `SKILL.md` and `package.json` files for each skill.

## Required Python Dependencies

Install these Python packages to use the skills:

```bash
python3 -m pip install --break-system-packages ddgs resend
```

## Security Considerations

The JavaScript adapters include proper input validation and sanitization to prevent command injection vulnerabilities when passing user input to shell commands.