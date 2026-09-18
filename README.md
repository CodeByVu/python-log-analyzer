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
* Accepts an optional keyword as a command-line argument
* Counts how many lines contain the supplied keyword

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

The keyword search counts how many lines contain the supplied keyword.

You can analyze a different log file:

```bash
python log_analyzer.py test.log
```

If no log filename is provided, the program displays an error message and exits.

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
When a keyword is provided, the analyzer also reports the number of matching lines:

KEYWORD MATCHES: 3

## 🚧 Current Limitations

The project is still under development.

At the moment:

* The analyzer expects the log level to be the first word on each line
* Only the log levels `INFO`, `WARNING`, `ERROR`, and `DEBUG` are recognized automatically
* Other log levels are categorized as `UNKNOWN`
* Missing or invalid files are not yet handled gracefully
* Keyword searches currently report the number of matching lines but do not display the matching lines

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

The analyzer now accepts a log filename from the command line and optionally accepts a keyword to search for. It counts the number of lines containing the supplied keyword while continuing to perform the original log-level analysis.

The next improvement is displaying the actual lines that match a supplied keyword.
