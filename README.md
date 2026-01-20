# SSL Certificate Checker (Python)

A simple command-line tool that checks a website's SSL certificate and prints:

- Valid / expired status
- Expiry date (UTC)
- Issuer organization
- Subject common name

---

## Requirements

- Python 3.8+

No extra external packages required — this uses Python’s standard library (`socket`, `ssl`, `datetime`).

---

## Install & Run

Clone or download this repository, then run:

```bash
python src/cli.py

Example
Input:
example.com

Output:

Status: VALID
Valid until (UTC): 2026-01-01 12:00:00
Issuer (organizationName): Let's Encrypt
Subject (commonName): example.com
