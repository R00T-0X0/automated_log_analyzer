# Automated Log Analyzer

A Python-based security log analysis tool designed to detect suspicious activities and potential web application attacks by analyzing log files using Regular Expressions.

## Features

- **SQL Injection Detection:** Identifies suspicious SQL injection patterns, including `UNION SELECT` and SQL-based expressions.
- **Path Traversal Detection:** Detects attempts to access restricted files and directories, such as `../etc/passwd`.
- **Cross-Site Scripting (XSS) Detection:** Identifies potentially malicious scripts, JavaScript URLs, and suspicious HTML event handlers.
- **Potential CSRF Detection:** Identifies suspicious state-changing requests that may indicate missing CSRF protection.
- **IP Address Extraction:** Extracts the source IP address associated with suspicious log entries.
- **Line Number Tracking:** Reports the exact line where suspicious activity is detected.
- **Attack Summary:** Displays the total number of detected events for each attack category.
- **Regular Expression Matching:** Uses Python's `re` module for pattern-based detection.
- **Line-by-Line Processing:** Reads log files efficiently without loading the entire file into memory.

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- File Handling
- IP Address Extraction
- Command-Line Interface (CLI)

## Project Structure

```text
Automated-Log-Analyzer/
│
├── automated_log_analyzer.py
├── test_logs.txt
└── README.md
```

## Requirements

- Python 3.x
- No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/R00T-0X0/Automated-Log-Analyzer.git
```

Navigate to the project directory:

```bash
cd Automated-Log-Analyzer
```

## Usage

Run the tool by providing a log file as an argument:

```bash
python automated_log_analyzer.py test_logs.txt
```

You can also analyze other supported log files:

```bash
python automated_log_analyzer.py access.log
```

## Example Test Logs

The following entries can be used to test the detection functionality:

```text
192.168.1.10 - - "GET /index.php HTTP/1.1" 200
192.168.1.15 - - "GET /products?id=1 UNION SELECT username,password FROM users HTTP/1.1" 200
192.168.1.20 - - "GET /../../etc/passwd HTTP/1.1" 403
192.168.1.25 - - "GET /search?q=<script>alert(1)</script> HTTP/1.1" 200
192.168.1.30 - - "POST /account/change-password HTTP/1.1" 200
```

## Detection Categories

| Attack Type | Description |
|---|---|
| SQL Injection | Detects suspicious SQL injection patterns. |
| Path Traversal | Detects attempts to access restricted system files. |
| XSS | Detects potentially malicious scripts and JavaScript content. |
| Potential CSRF | Identifies suspicious requests that may lack CSRF protection. |

## Detection Output

For each detected event, the tool reports:

- Attack category
- Source IP address
- Log line number
- Detection details

At the end of the analysis, a summary displays the number of detected events in each category.

## Security Note

This tool uses pattern-based detection and is intended for educational purposes, security monitoring practice, and basic log analysis.

Its results are indicators of suspicious activity, not definitive proof of an attack. In particular, CSRF cannot be reliably confirmed from ordinary access logs alone without additional application context.

## Author

**Bashar Almadhaji**

Cybersecurity | SOC Analysis | Security Monitoring

---

**Disclaimer:** Use this tool only on log files you are authorized to analyze.
