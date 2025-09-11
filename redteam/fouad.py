#!/usr/bin/env python3
import os, sys, pyfiglet
from colorama import Fore, Style, init
init(autoreset=True)

def print_logo():
    os.system("clear")
    text = "FOUAD TOOL"
    fig = pyfiglet.figlet_format(text, font="slant")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    for line in fig.split("\n"):
        for i,ch in enumerate(line):
            if ch.strip():
                print(colors[i%len(colors)] + ch, end=Style.RESET_ALL)
            else:
                print(" ", end="")
        print()
    print(Fore.YELLOW + "="*70)
    print(Fore.RED + " BlackHat Framework - Author: Fouad Zulof ")
    print(Fore.CYAN + " Instagram: " + Fore.MAGENTA + "@1.pvl")
    print(Fore.YELLOW + "="*70 + "\n")

# Ollama submenu
def ollama_menu():
    os.system("clear")
    print_logo()
    print(Fore.MAGENTA + "╔" + "═"*50 + "╗")
    models = os.popen("ollama list").read().splitlines()

    if not models:
        print(Fore.RED + "[-] No Ollama models installed. Use 'ollama pull <model>' first.")
        input(Fore.CYAN + "Press ENTER to return...")
        return

    for idx, m in enumerate(models, start=1):
        parts = m.split()
        model_name = parts[0]
        print(Fore.MAGENTA + "║" + Fore.YELLOW + f"{idx:02d}. {model_name:<45}" + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚" + "═"*50 + "╝")
    print(Fore.RED + "\n00. Back\n")

    try:
        choice = int(input(Fore.GREEN + "[Select Model Number] > "))
        if choice == 0:
            return
        elif 1 <= choice <= len(models):
            model = models[choice-1].split()[0]
            os.system(f"ollama run {model}")
        else:
            print(Fore.RED + "Invalid choice...")
    except ValueError:
        print(Fore.RED + "Enter valid number.")

    input(Fore.CYAN + "Press ENTER to return...")

# Main tools
tools = [
    ("hiden service", "OLLAMA_SUBMENU"),
    ("Nmap Scanner", "nmap -A "),
    ("Netcat Banner Grab", "nc -v "),
    ("Traceroute", "traceroute "),
    ("Ping", "ping -c 4 "),
    ("Tcpdump Sniffer", "tcpdump -i any -c 10"),
    ("Wireshark (tshark)", "tshark -i any -c 10"),
    ("ARP Spoofing", "arpspoof -t "),
    ("Bettercap", "bettercap"),
    ("SQLmap", "sqlmap -u "),
    ("Nikto Web Scanner", "nikto -h "),
    ("Gobuster DirBuster", "gobuster dir -u "),
    ("WFuzz", "wfuzz -u "),
    ("WPScan", "wpscan --url "),
    ("WhatWeb", "whatweb "),
    ("Curl Headers", "curl -I "),
    ("SSLScan", "sslscan "),
    ("John the Ripper", "john "),
    ("Hashcat", "hashcat "),
    ("fcrackzip", "fcrackzip "),
    ("Hydra", "hydra "),
    ("Crunch Wordlist", "crunch 4 6 abc123 -o wordlist.txt"),
    ("Base64 Encode", "base64 "),
    ("Base64 Decode", "base64 -d "),
    ("URL Encode", "python3 -m urllib.parse quote "),
    ("URL Decode", "python3 -m urllib.parse unquote "),
    ("Metasploit Console", "msfconsole"),
    ("MSFVenom Payload", "msfvenom "),
    ("SearchSploit", "searchsploit "),
    ("Socat ReverseShell", "socat "),
    ("WHOIS", "whois "),
    ("theHarvester", "theHarvester -d "),
    ("Dnsenum", "dnsenum "),
    ("Dnsmap", "dnsmap "),
    ("Sublist3r", "sublist3r -d "),
    ("Amass", "amass enum -d "),
    ("Dirsearch", "dirsearch -u "),
    ("FFUF", "ffuf -u "),
    ("XSStrike", "xsstrike -u "),
    ("Commix (Command Injection)", "commix --url="),
    ("Sqliv", "sqliv -t "),
    ("Recon-ng", "recon-ng"),
    ("Maltego", "maltego"),
    ("Enum4linux", "enum4linux "),
    ("SMBMap", "smbmap -H "),
    ("CrackMapExec", "crackmapexec "),
    ("Responder", "responder -I "),
    ("Impacket-SmbExec", "psexec.py "),
    ("Kerbrute", "kerbrute userenum "),
    ("BloodHound", "bloodhound"),
    ("Bettercap full MITM", "bettercap -X"),
]

def menu():
    while True:
        print_logo()
        print(Fore.MAGENTA + "╔" + "═"*70 + "╗")

        half = len(tools)//2
        for i in range(half):
            left_name = f"{i+1:02d}. {tools[i][0]}"
            right_name = f"{i+half+1:02d}. {tools[i+half][0]}"
            print(Fore.MAGENTA + "║" + Fore.YELLOW + f"{left_name:<33} {right_name:<33}" + Fore.MAGENTA + "║")

        print(Fore.MAGENTA + "╚" + "═"*70 + "╝")
        print(Fore.RED + "\n00. Exit\n")

        try:
            choice = int(input(Fore.GREEN + "[Select Tool Number] > "))
            if choice == 0:
                print(Fore.RED + "\nExiting... Stay in the shadows 😈\n")
                sys.exit(0)
            elif 1 <= choice <= len(tools):
                cmd = tools[choice-1][1]
                if cmd == "OLLAMA_SUBMENU":
                    ollama_menu()
                else:
                    arg = input(Fore.CYAN + f"Enter args for {tools[choice-1][0]}: ")
                    os.system(cmd + arg)
            else:
                print(Fore.RED + "Invalid choice...")
        except ValueError:
            print(Fore.RED + "Enter valid number.")

        input(Fore.CYAN + "Press ENTER to return...")

if __name__=="__main__":
    menu()
