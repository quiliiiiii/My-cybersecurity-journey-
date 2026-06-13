# Log Analyzer v2

## Overview

This project is a Python-based security log analyzer. It reads a sample authentication log file and identifies failed login attempts, successful logins, and suspicious IP addresses.

## Why I Built This

As a cybersecurity student, I wanted to understand how security analysts review logs to detect suspicious activity. Log analysis is an important skill in SOC, incident response, and threat detection.

## Features

- Reads authentication logs
- Detects failed SSH login attempts
- Counts failed attempts per IP address
- Identifies suspicious IPs
- Generates a simple security report

## Files

- `log_analyzer.py` — Python script
- `sample.log` — sample log file for testing
- `README.md` — project explanation

## What I Learned

Through this project, I learned how Python can be used to automate security monitoring tasks. I also learned how failed login attempts can indicate brute-force activity.

## Future Improvements

- Export results to a report file
- Add severity levels
- Analyze real Linux authentication logs
- Create a web dashboard using HTML and CSS
