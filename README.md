# CodeAlpha Secure Coding Review

## Project Overview

This project was completed as part of the CodeAlpha Cyber Security Internship.

The project demonstrates a secure coding review of a Python-based Login Application. An intentionally vulnerable application was created and analyzed using manual code review and the Bandit security scanner. The identified security weaknesses were then remediated in a secure version of the application.

## Technology Used

- Python 3.12
- Bandit 1.9.4
- Visual Studio Code
- Windows

## Project Structure

```text
CodeAlpha_SecureCodingReview
├── login_app.py
├── secure_login_app.py
└── README.md


## Vulnerable Application

The initial application contained intentional security weaknesses for the purpose of security testing.

### Vulnerabilities Identified

1. **Hardcoded Password**
   - The password was directly stored in the source code.
   - Bandit detected this as `B105: hardcoded_password_string`.
   - CWE: CWE-259.

2. **Password Disclosure**
   - The application displayed the entered password as debug information.
   - Passwords should never be displayed or logged.

3. **Weak Password**
   - The example password was weak and easy to guess.
   - Strong passwords should be used in real applications.

## Security Tool

Bandit was used to perform static security analysis of the Python source code.

### Vulnerable Code Scan

Bandit detected:

```text
B105: hardcoded_password_string
Severity: Low
Confidence: Medium
CWE-259
