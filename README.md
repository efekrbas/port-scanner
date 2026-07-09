# Port Scanner

A fast, multi-threaded port scanner built with Python.

## Features
- Scans a specified IP address or domain name for open ports.
- Uses multi-threading (`concurrent.futures.ThreadPoolExecutor`) for blazing fast concurrent scanning.
- Validates IP addresses and resolves domain names to prevent errors.
- Customizable port range scanning.

## Usage
Run the script using Python:
```bash
python portscanner.py
```

Follow the on-screen prompts to enter the target IP address or domain name and the range of ports you want to scan.

## Source / Inspiration
This project was built following the concepts from this tutorial video: 
[Python Port Scanner Tutorial](https://www.youtube.com/watch?v=qqB6e_g2Oas)