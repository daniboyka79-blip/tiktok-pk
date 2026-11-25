#!/data/data/com.termux/files/usr/bin/env python
import os
import sys
import time
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

REPO_DIR = os.path.expanduser("~/tiktok-pk")

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

class ReusableServer(HTTPServer):
    allow_reuse_address = True

def start_server():
    print(f"\n{GREEN}[+] TikTok PK Simulator ተጀምሯል!{RESET}")
    print(f"{YELLOW}[*] ብራውዘርህን (Chrome) ከፍተህ ይህን ሊንክ አስገባ:{RESET}")
    print(f"{CYAN}    http://127.0.0.1:8080{RESET}")
    print(f"{RED}[*] ለማቆም CTRL + C ተጫን።{RESET}\n")
    server = ReusableServer(("127.0.0.1", 8080), QuietHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\n[!] Server ቆሟል።")

def update_github():
    print(f"\n{YELLOW}[*] ከ GitHub በማደስ ላይ...{RESET}")
    res = subprocess.check_output(["git", "-C", REPO_DIR, "pull"], stderr=subprocess.STDOUT)
    print(f"{GREEN}[+] {res.decode().strip()}{RESET}")
    time.sleep(1)

def main():
    while True:
        os.system("clear")
        print(f"{CYAN}=== TikTok LIVE PK Simulator (GitHub + Termux) ==={RESET}\n")
        choice = input("[s] Start Simulator  [u] Update (GitHub)  [q] Quit > ").strip().lower()
        if choice == "s":
            start_server()
        elif choice == "u":
            update_github()
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
