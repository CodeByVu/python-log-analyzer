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

## 💻 Current Usage

The program currently analyzes a file named `app.log`.

Run it with:

```bash
python log_analyzer.py
```

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

## 🚧 Current Limitations

The project is still under development.

At the moment:

* The input file is hard-coded as `app.log`
* The analyzer expects the log level to be the first word on each line
* Only the log levels `INFO`, `WARNING`, `ERROR`, and `DEBUG` are recognized automatically
* Other log levels are categorized as `UNKNOWN`

These limitations will be addressed as the project develops.

## 🛠️ Technologies

* Python
* Git
* GitHub
* GitHub Codespaces
* VS Code

## 🎯 Project Goals

Future development may include:

* Allowing users to provide their own log filename
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

> [!NOTE]
> This is an evolving learning project. Features are added incrementally with an emphasis on understanding the code and development process rather than simply producing a finished application.

## 📌 Project Status

🚧 **Actively developing**

The next major improvement is allowing the user to specify which log file the analyzer should process instead of always using `app.log`.
