# 🐍 Python Log Analyzer

A beginner-friendly Python command-line utility for analyzing text-based log files.

This project is being built incrementally as a hands-on Python and IT learning project. The goal is to eventually turn it into a more reusable log-analysis tool for troubleshooting and basic log investigation.

## ✨ Current Features

* Counts `INFO`, `WARNING`, `ERROR`, and `DEBUG` log entries
* Identifies the log level from the beginning of each line
* Detects and counts unrecognized log levels as `UNKNOWN`
* Calculates the percentage of entries in each category
* Reports the total number of entries analyzed
* Reads the log file line by line using Python file handling
* Skips blank lines during analysis
* Accepts an optional keyword as a command-line argument
* Searches each line for the supplied keyword
* Displays and numbers matching lines
* Reports the total number of keyword matches

## 💻 Current Usage

The program accepts the log filename as a required command-line argument and an optional keyword for searching.

Run it with a log file only:

```bash
python log_analyzer.py app.log
```

You can also search the log for a keyword:
```bash
python log_analyzer.py app.log database
```

The keyword search displays each matching line and reports the total number of matching lines.

You can analyze a different log file:
```bash
python log_analyzer.py test.log
```

If no log filename is provided, the program displays an error message and exits.

If no keyword is provided, the program skips the keyword search and continues with the normal log analysis.

### Example Output

```text
INFO: 3
WARNING: 2
ERROR: 3
DEBUG: 1
UNKNOWN: 1
TOTAL: 10
INFO PCT: 30.0%
WARNING PCT: 20.0%
ERROR PCT: 30.0%
DEBUG PCT: 10.0%
UNKNOWN PCT: 10.0%
```
When a keyword is provided and matches are found:

```text
MATCH #1:
Database connection failed

MATCH #2:
Database response time exceeded

KEYWORD MATCHES: 2

When a keyword is provided but no matches are found:

KEYWORD MATCHES: 0
```

## 🚧 Current Limitations

The project is still under development.

At the moment:

* The analyzer expects the log level to be the first word on each line
* Only the log levels `INFO`, `WARNING`, `ERROR`, and `DEBUG` are recognized automatically
* Other log levels are categorized as `UNKNOWN`
* Missing or invalid files are not yet handled gracefully
* Keyword searches currently use a simple substring search, so the keyword can match part of a larger word

These limitations will be addressed as the project develops.

## 🛠️ Technologies

* Python
* Git
* GitHub
* GitHub Codespaces
* VS Code

## 🎯 Project Goals

Future development may include:

* Handling missing or invalid files
* Supporting additional log formats
* More detailed statistics and summaries
* Filtering and searching log entries
* JSON output
* Automated testing
* Improved documentation

## 📚 Learning Focus

This project is being developed as a practical way to learn Python programming and problem-solving.

Concepts currently practiced include:

* Variables
* Conditional statements
* `if` / `elif` / `else`
* Nested `if` statements
* `for` loops
* String methods
* Lists and indexing
* File handling
* Counters and arithmetic
* f-strings
* Basic error handling and debugging
* Git version control
* Command-line arguments with `sys.argv`
* `None` and optional values

> [!NOTE]
> This is an evolving learning project. Features are added incrementally with an emphasis on understanding the code and development process rather than simply producing a finished application.

## 📌 Project Status

🚧 **Actively developing**

The analyzer accepts a log filename from the command line and optionally accepts a keyword to search for. It performs the original log-level analysis while also displaying and counting lines that contain the supplied keyword.

The next improvement is handling missing or invalid file paths more gracefully.
