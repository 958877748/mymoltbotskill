"""
Resend Mail Skill - Package Init

This module provides functions to send emails using the Resend API.
"""

from .send_mail import skill_resend_mail, send_email

__all__ = [
    'skill_resend_mail',
    'send_email'
]

__version__ = "1.0.0"
__author__ = "Assistant"