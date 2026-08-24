# CodeAlpha Secure Coding Review

## Project Overview

This project was completed as part of the CodeAlpha Cyber Security Internship.

The project demonstrates a secure coding review of a Python-based Login Application. An intentionally vulnerable application was created and analyzed using manual code review and the Bandit security scanner. The identified security weaknesses were then remediated in a secure version of the application.

## Technology Used

- Python 3.12
- Bandit
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

1. Hardcoded Password
   - The password was directly stored in the source code.
   - Bandit detected this as B105: hardcoded_password_string.
   - CWE-259.

2. Password Disclosure
   - The application displayed the entered password as debug information.
   - Passwords should never be displayed or logged.

3. Weak Password
   - The example password was weak and easy to guess.
   - Strong passwords should be used in real applications.

## Security Tool

Bandit was used to perform static security analysis of the Python source code.

### Vulnerable Code Scan

Bandit detected:

B105: hardcoded_password_string
Severity: Low
Confidence: Medium
CWE-259

## Remediation

A secure version of the application was created in secure_login_app.py.

The improvements include:

- Removed the hardcoded plain-text password.
- Used password hashing with PBKDF2-HMAC.
- Used a random salt.
- Used getpass to prevent the password from being displayed while entering it.
- Removed password debug output.
- Added verification using the password hash.

## Secure Code Scan

The secure version was scanned again using Bandit.

Result: No issues identified.

Bandit reported:

- High: 0
- Medium: 0
- Low: 0
- Undefined: 0

## Testing

The vulnerable application was tested successfully.

The secure application was also tested successfully. The secure application hides the password during input and does not display it after login.

## Security Best Practices

- Never hardcode passwords or other sensitive credentials.
- Never print or log passwords.
- Use strong passwords.
- Store passwords using secure password hashing.
- Use a unique salt when hashing passwords.
- Perform static security analysis during development.
- Combine automated tools with manual security review.
- Avoid exposing sensitive information through debug messages.

## Conclusion

This project demonstrates how secure coding practices can improve the security of a Python login application. Manual code review identified security weaknesses, while Bandit provided automated static analysis. After remediation, the secure version successfully passed the Bandit scan with no issues identified.
