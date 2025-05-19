#!/usr/bin/env python3
"""
Passive Recon Framework – All-in-One Script

Dependencies:
    pip install requests ipwhois markdown
Environment Variables (optional for enhanced features):
    SECURITYTRAILS_API_KEY  - API key for SecurityTrails subdomain lookup
    GITHUB_TOKEN            - Personal access token for GitHub Search API

"""
import argparse
import os
import sys
import time
import socket
import re
import json
import requests
from ipwhois import IPWhois
import markdown

# ---- Subdomain Enumeration ----
def enumerate_subdomains(domain:
    str) -> list:
    subs = set()
    api_key = os.getenv('SECURITYTRAILS_API_KEY')
    if api_key:
        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        headers = {'APIKEY': api_key}
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            data = resp.json()
            for s in data.get('subdomains', []):
                subs.add(f"{s}.{domain}")
            print(f"[+] SecurityTrails: {len(data.get('subdomains', []))} subdomains")
        except Exception as e:
            print(f"[!] SecurityTrails error: {e}")
    # CRT.sh fallback
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        resp = requests.get(url, timeout=10)
        entries = resp.json()
        for e in entries:
            name = e.get('name_value','')
            for sub in name.split('\n'):
                if '*' not in sub:
                    subs.add(sub.strip())
        print(f"[+] crt.sh: {len(entries)} certificates parsed")
    except Exception as e:
        print(f"[!] crt.sh error: {e}")
    return sorted(subs)

# ---- ASN Lookup ----
def lookup_asn(domain: str) -> dict:
    results = {}
    try:
        infos = socket.getaddrinfo(domain, None)
        ips = {info[4][0] for info in infos}
    except Exception:
        print(f"[!] DNS resolution failed for {domain}")
        ips = set()
    for ip in ips:
        try:
            obj = IPWhois(ip)
            rdap = obj.lookup_rdap(depth=1)
            asn = rdap.get('asn')
            net = rdap.get('network',{}).get('cidr')
            results[ip] = {'asn': asn, 'network': net}
        except Exception as e:
            results[ip] = {'error': str(e)}
    return results

# ---- GitHub Exposures ----
def find_github_exposures(domain: str) -> list:
    exposures = []
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'
    q = f"{domain}+in:file"
    url = f"https://api.github.com/search/code?q={q}&per_page=30"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        for item in data.get('items', []):
            exposures.append(item.get('html_url'))
        print(f"[+] GitHub: {len(exposures)} results")
    except Exception as e:
        print(f"[!] GitHub API error: {e}")
    return exposures

# ---- LinkedIn Scraping (via Bing) ----
def scrape_linkedin(domain: str) -> list:
    profiles = set()
    query = f"site:linkedin.com/in {domain}"
    url = f"https://www.bing.com/search"
    params = {'q': query}
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        links = re.findall(r'href=\"(https?://[^"]+linkedin.com/in/[^"]+)\"', resp.text)
        for link in links:
            profiles.add(link)
        print(f"[+] LinkedIn: {len(profiles)} profiles")
    except Exception as e:
        print(f"[!] LinkedIn search error: {e}")
    return sorted(profiles)

# ---- Report Generation ----
def generate_report(domain: str, subdomains: list, asn_data: dict,
                    github_exposures: list, linkedin_profiles: list,
                    output_path: str) -> None:
    md = [f"# Passive Recon Report: {domain}\n"]
    md.append("## Subdomains\n")
    for s in subdomains:
        md.append(f"- {s}\n")
    md.append("\n## ASN Data\n")
    md.append('```json\n' + json.dumps(asn_data, indent=2) + '\n```\n')
    md.append("## GitHub Exposures\n")
    for url in github_exposures:
        md.append(f"- {url}\n")
    md.append("## LinkedIn Profiles\n")
    for url in linkedin_profiles:
        md.append(f"- {url}\n")
    content = ''.join(md)
    if output_path.endswith('.html'):
        html = markdown.markdown(content)
        with open(output_path, 'w') as f:
            f.write(html)
    else:
        with open(output_path, 'w') as f:
            f.write(content)

# ---- Main ----
def main():
    parser = argparse.ArgumentParser(description="Passive Recon All-in-One")
    parser.add_argument('-d', '--domain', required=True, help='Target domain')
    parser.add_argument('-o', '--output', default='report.md', help='Report file (.md/.html)')
    args = parser.parse_args()

    domain = args.domain
    print(f"[+] Starting passive recon for: {domain}\n")

    subs = enumerate_subdomains(domain)
    print(f"[+] Total subdomains: {len(subs)}\n")
    time.sleep(1)

    asn_data = lookup_asn(domain)
    time.sleep(1)

    github = find_github_exposures(domain)
    time.sleep(1)

    linkedin = scrape_linkedin(domain)

    print("\n[+] Generating report...")
    generate_report(domain, subs, asn_data, github, linkedin, args.output)
    print(f"[+] Report saved to {args.output}")

if __name__ == '__main__':
    main()
