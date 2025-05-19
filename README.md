reconFramework

A comprehensive, all-in-one Python script for passive reconnaissance and OSINT data collection targeting domains. Ideal for pentesters, bug bounty hunters, and security researchers.

Features

Subdomain Enumeration

Uses SecurityTrails API (if SECURITYTRAILS_API_KEY provided)

crt.sh certificate scraping fallback

ASN & IP Information

Resolves domain to IPs

Queries RDAP via ipwhois for ASN and network CIDR

GitHub Exposure Search

Uses GitHub Search API (if GITHUB_TOKEN provided)

Finds code snippets and potential leaks referencing the domain

LinkedIn Profile Discovery

Performs Bing search for site:linkedin.com/in <domain>

Collects public LinkedIn profile URLs

Report Generation

Outputs a Markdown (.md) or HTML (.html) report

Consolidates all findings in an easy-to-read format

Prerequisites

Python 3.6+

PIP dependencies:

pip install requests ipwhois markdown

Environment variables (optional but recommended):

SECURITYTRAILS_API_KEY — SecurityTrails API key for subdomain enumeration

GITHUB_TOKEN — GitHub personal access token for code search

Installation

Clone the repository:

git clone https://github.com/yourusername/reconFramework.git
cd reconFramework

(Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the script with the target domain and desired output file:

python3 reconFramework.py -d example.com -o report.md

To generate HTML instead of Markdown, specify -o report.html.

Ensure environment variables are set for enhanced features:

export SECURITYTRAILS_API_KEY="your_key"
export GITHUB_TOKEN="your_token"

Example

$ python3 reconFramework.py -d example.com -o example_report.md
[+] Starting passive recon for: example.com
[+] SecurityTrails: 42 subdomains
[+] crt.sh: Parsed 15 certificates
[+] Total subdomains: 43
[+] DNS resolution: success
[+] ASN data collected for 2 IPs
[+] GitHub: 5 results
[+] LinkedIn: 3 profiles
[+] Generating report...
[+] Report saved to example_report.md

License

MIT License © 2025 Your Name

Contributing

Contributions are welcome! Please open issues or submit pull requests on GitHub.
