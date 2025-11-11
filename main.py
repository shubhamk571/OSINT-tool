#!/usr/bin/env python3
"""
OSINT Intelligence Gathering Tool
---------------------------------
Performs automated reconnaissance and generates a consolidated intelligence report.
"""

import argparse
from modules import whois_lookup, dns_lookup, email_lookup, social_media
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="OSINT Intelligence Gathering Tool")
    parser.add_argument("--domain", help="Target domain for intelligence gathering")
    parser.add_argument("--email", help="Target email address for intelligence gathering")
    parser.add_argument("--username", help="Username to check across social media")
    parser.add_argument("--output", default="osint_report.json", help="Output report file")

    args = parser.parse_args()

    results = {}

    if args.domain:
        print(f"[+] Running WHOIS lookup for {args.domain}")
        results["whois"] = whois_lookup.get_whois_info(args.domain)

        print(f"[+] Running DNS lookup for {args.domain}")
        results["dns"] = dns_lookup.get_dns_info(args.domain)

    if args.email:
        print(f"[+] Checking email intelligence for {args.email}")
        results["email"] = email_lookup.check_email(args.email)

    if args.username:
        print(f"[+] Checking social media profiles for {args.username}")
        results["social_media"] = social_media.check_profiles(args.username)

    print("[+] Generating report...")
    generate_report(results, args.output)
    print(f"[✓] Report saved as {args.output}")

if __name__ == "__main__":
    main()
