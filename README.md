Pasive Recon Framework

It is just recon framework help you to get info on victum and it make a file and add all of this to help you share info with your team

Note you should use and virtual environment and install requirments.txt

Usage:

python3 reconFramework.py -d example.com -o report.md

Simple output from testing example.com

``` bash
(venv) ziad686@DESKTOP-9DQQS7O:/mnt/d/reconFramework$ python3 ./reconFramework.py -d example.com -o report.md
[+] Starting passive recon for: example.com

[+] crt.sh: 33 certificates parsed
[+] Total subdomains: 10

[+] GitHub: 0 results
[+] LinkedIn: 0 profiles

[+] Generating report...
[+] Report saved to report.md
(venv) ziad686@DESKTOP-9DQQS7O:/mnt/d/reconFramework$ cat ./report.md
# Passive Recon Report: example.com
## Subdomains
- AS207960 Test Intermediate - example.com
- dev.example.com
- example.com
- m.example.com
- m.testexample.com
- products.example.com
- subjectname@example.com
- support.example.com
- user@example.com
- www.example.com

## ASN Data
```json
{
  "2600:1408:ec00:36::1736:7f24": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "23.215.0.138": {
    "asn": "20940",
    "network": "23.192.0.0/11"
  },
  "2600:1406:bc00:53::b81e:94ce": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "2600:1406:3a00:21::173e:2e66": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "2600:1406:bc00:53::b81e:94c8": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "23.192.228.84": {
    "asn": "20940",
    "network": "23.192.0.0/11"
  },
  "23.192.228.80": {
    "asn": "20940",
    "network": "23.192.0.0/11"
  },
  "2600:1406:3a00:21::173e:2e65": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "96.7.128.175": {
    "asn": "20940",
    "network": "96.6.0.0/15"
  },
  "96.7.128.198": {
    "asn": "20940",
    "network": "96.6.0.0/15"
  },
  "2600:1408:ec00:36::1736:7f31": {
    "asn": "20940",
    "network": "2600:1400::/24"
  },
  "23.215.0.136": {
    "asn": "20940",
    "network": "23.192.0.0/11"
  }
}
```
```
## GitHub Exposures
## LinkedIn Profiles
(venv) ziad686@DESKTOP-9DQQS7O:/mnt/d/reconFramework$
```
