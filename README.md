# HTTP Login Tester

A simple Python tool for testing HTTP login authentication.

## Description

This project is a Python script that sends login requests to an HTTP endpoint using usernames and passwords provided manually or through wordlists.

Created for educational purposes and authorized security testing.

## Features

- Test a single username or a username wordlist
- Test a single password or a password wordlist
- Send HTTP POST requests using Python Requests
- Session handling

## Requirements

- Python 3.x
- Requests library

Install the required library:

```bash
pip install requests
```
## Configuration

- Add your wordlists in the main directory or use a public wordlist.
- You can modify the variable names in the payload directly in the code. You can find the correct parameter names by checking the website requests in the browser developer tools (F12).
  
## Usage

Run the script:

```bash
python script.py
```

Follow the instructions shown in the terminal.

## Disclaimer

This tool is intended only for educational purposes and authorized security assessments.

Do not use this tool against systems without explicit permission.
