FOUAD TOOL — Educational Network Analysis Toolkit

A lightweight, educational project for learning network traffic analysis and building safe, legal lab environments.
This repository is for research and teaching only. — Use only on datasets and environments you own or where you have explicit permission.

🔥 What this is

FOUAD TOOL is an educational toolkit and menu-driven interface intended to help students and researchers learn about network traffic, packet analysis, and defensive monitoring techniques.
It does not provide or enable offensive operations. Any offensive commands that might appear in the original menu are placeholders and should remain disabled in this repository. The primary safe component included is a PCAP analyzer that reads local .pcap files and produces human-readable statistics for research and reporting.

⚠️ Legal & Ethical Notice (READ BEFORE USING)

By using this software you agree: you will only run it on files, captures, or test environments that you own or for which you have written permission.

Do NOT use this software to attack, probe, scan, or compromise systems or networks that you do not own or are not authorized to test.

The author and contributors are not responsible for misuse. Any illegal or unethical activity is strictly prohibited.

This project is intended for educational, defensive, and research purposes only. If you are unsure whether a planned activity is legal, obtain written authorization or consult a legal advisor.

Add this repository to your university submission only after including the required approvals and a description of the safe testbed used (VM images, isolated network, or captive datasets).

✅ Safe Features

neon_analyzer.py — PCAP analysis script (safe). Reads local .pcap captures and prints:

total packets, average packet length

top source/destination IPs

protocol distribution

most common TCP/UDP destination ports

Menu-driven UI (display-only) for organizing analysis tools and launching safe modules or local viewers.

Documentation, usage examples, and a sample dataset (optional) for teaching.

📥 Requirements

Tested with Python 3.8+.

Python packages:
