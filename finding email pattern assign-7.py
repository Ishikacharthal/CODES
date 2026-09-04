"""
===============================================================
EMAIL PATTERN FINDER USING REGULAR EXPRESSIONS
===============================================================

In simple words:

A regular expression (regex) is a search pattern.
Instead of searching for one exact email address,
we describe the SHAPE of an email address.

Example:
rahul_23@gmail.com

The pattern looks for:
characters + @ + domain + . + suffix
"""

import re


# =============================================================
# 1. EMAIL PATTERN
# =============================================================
# In simple words:
# Before @  → letters, numbers, _, ., +, -
# @         → must contain @
# After @   → letters, numbers, -
# \.        → must contain a real dot
# Last part → letters, numbers, ., -

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


# =============================================================
# 2. FIND ALL EMAILS IN A BLOCK OF TEXT
# =============================================================
# This function searches the complete text
# and returns all email addresses it finds.

def find_emails(text):
    """
    Find all email addresses from the given text.
    """
    return re.findall(EMAIL_PATTERN, text)


# =============================================================
# 3. VALIDATE ONE EMAIL ADDRESS
# =============================================================
# This function checks whether the complete string
# is a valid email according to our pattern.

def is_valid_email(candidate):
    """
    Return True if the complete string is a valid email.
    Otherwise return False.
    """
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# =============================================================
# 4. MAIN PROGRAM / DEMONSTRATION
# =============================================================

if __name__ == "__main__":

    # Sample text containing different email addresses
    sample_text = """
    Please contact us for support:
    - General queries: support@examplecorp.com
    - Sales team: sales.team@business-hub.co.in
    - Personal note from Rahul (rahul_23@gmail.com) sent yesterday.
    - Invalid mentions: not-an-email, @missing-local.com, plain.text@
    - Newsletter sign-up: newsletter+promo@my-site.org
    """

    # ---------------------------------------------------------
    # Find all emails in the sample text
    # ---------------------------------------------------------

    print("Original text:")
    print(sample_text)

    found = find_emails(sample_text)

    print(f"\nFound {len(found)} email address(es) in the text:")

    for email in found:
        print(f" - {email}")


    # ---------------------------------------------------------
    # Validate individual email addresses
    # ---------------------------------------------------------

    print("\nValidating individual strings with is_valid_email():")

    test_cases = [
        "john.doe@example.com",
        "invalid-email",
        "user@site",
        "user@site.com",
        "plain.text@",
        "a.b-c_d+e@sub.domain.co.in",
    ]

    # Check every email one by one
    for candidate in test_cases:

        result = "VALID" if is_valid_email(candidate) else "INVALID"

        print(f"{candidate:30s} -> {result}")