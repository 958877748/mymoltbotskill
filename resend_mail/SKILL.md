---
name: resend_mail
description: Send emails using the Resend API service.
---

# Resend Mail

Send emails using the Resend API service with your API key.

## Setup

Set your Resend API key as an environment variable:

```bash
export RESEND_API_KEY="your_api_key_here"
```

Or pass the API key as a parameter when calling the skill.

## Usage

```bash
python send_mail.py --to "recipient@example.com" --subject "Hello" --body "Hello from Resend!"
```

## Features

- Send HTML emails via Resend API
- Configurable sender and recipient addresses
- Error handling for failed deliveries
- Message ID tracking

## Dependencies

- resend (installed via pip)

## When to Use

- When you need to send transactional emails
- For automated email notifications
- When you want reliable email delivery
- For sending emails from scripts or automation