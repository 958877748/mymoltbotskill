#!/usr/bin/env python3
"""
Resend Mail Skill
Send emails using the Resend API
"""

import resend
import argparse
import sys
import os


def send_email(api_key, to_email, subject, body, from_email="onboarding@resend.dev"):
    """
    Send an email using Resend API
    
    Args:
        api_key (str): Resend API key
        to_email (str): Recipient email address
        subject (str): Email subject
        body (str): Email body content
        from_email (str): Sender email address (default: onboarding@resend.dev)
    
    Returns:
        dict: Response from the API
    """
    try:
        # Set the API key
        resend.api_key = api_key
        
        # Prepare the email parameters
        params = {
            "from": from_email,
            "to": to_email,
            "subject": subject,
            "html": body
        }
        
        # Send the email
        email = resend.Emails.send(params)
        
        return {
            "success": True,
            "message_id": email["id"],
            "message": f"Email sent successfully to {to_email}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to send email: {str(e)}"
        }


def skill_resend_mail(to_email, subject, body, from_email="onboarding@resend.dev", api_key=None):
    """
    Main skill function to send email via Resend
    
    Args:
        to_email (str): Recipient email address
        subject (str): Email subject
        body (str): Email body content
        from_email (str): Sender email address
        api_key (str): Resend API key (can also be read from environment)
    
    Returns:
        str: Result message
    """
    # Get API key from parameter or environment variable
    if not api_key:
        api_key = os.getenv("RESEND_API_KEY")
    
    if not api_key:
        return "Error: No API key provided. Please set the RESEND_API_KEY environment variable or pass it as a parameter."
    
    result = send_email(api_key, to_email, subject, body, from_email)
    
    if result["success"]:
        return f"✅ Email sent successfully!\nMessage ID: {result['message_id']}\nTo: {to_email}\nSubject: {subject}"
    else:
        return f"❌ Failed to send email:\n{result['message']}"


def main():
    parser = argparse.ArgumentParser(description='Send emails using Resend API')
    parser.add_argument('--to', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body content')
    parser.add_argument('--from-email', default='onboarding@resend.dev', help='Sender email address')
    parser.add_argument('--api-key', help='Resend API key (optional if set as env var)')
    
    args = parser.parse_args()
    
    result = skill_resend_mail(
        to_email=args.to,
        subject=args.subject,
        body=args.body,
        from_email=args.from_email,
        api_key=args.api_key
    )
    
    print(result)


if __name__ == "__main__":
    main()