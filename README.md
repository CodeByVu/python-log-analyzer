# 🐍 Python Log Analyzer

A beginner-friendly Python command-line utility for analyzing text-based log files.

This project is being built incrementally as a hands-on Python and IT learning project. The goal is to turn Python concepts into practical programming experience while building a useful tool for troubleshooting and basic log investigation.

## ✨ Current Features

* Counts `INFO`, `WARNING`, `ERROR`, and `DEBUG` log entries
* Identifies the log level from the beginning of each line
* Detects and counts unrecognized log levels as `UNKNOWN`
* Calculates the percentage of entries in each category
* Reports the total number of entries analyzed
* Reads the log file line by line using Python file handling
* Skips blank lines during analysis
* Accepts a required log filename as a command-line argument
* Accepts an optional keyword as a command-line argument
* Searches each line for the supplied keyword
* Displays and numbers matching lines
* Reports the total number of keyword matches
* Handles missing log files with `FileNotFoundError`
* Separates reusable logic into functions
* Includes automated tests using `pytest`

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

If the specified log file cannot be found, the program displays an error message and exits cleanly.

If no keyword is provided, the program skips the keyword search and continues with the normal log analysis.

### Automated Tests

The project uses `pytest` to test the reusable functions.

Run the test suite with:

```bash
python -m pytest
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

When a keyword is provided and matches are found:

```text
MATCH #1:
Database connection failed

MATCH #2:
Database response time exceeded

KEYWORD MATCHES: 2
```

When a keyword is provided but no matches are found:

```text
KEYWORD MATCHES: 0
```

## 🚧 Current Limitations

The project intentionally keeps the log format and analysis logic simple.

At the moment:

* The analyzer expects the log level to be the first word on each line
* Only the log levels `INFO`, `WARNING`, `ERROR`, and `DEBUG` are recognized automatically
* Other log levels are categorized as `UNKNOWN`
* Keyword searches use a simple case-sensitive substring search, so the keyword can match part of a larger word
* Only missing files are explicitly handled; other file-related errors are not currently handled separately

These limitations leave room for future experimentation without making the current project unnecessarily complex.

## 🛠️ Technologies

* Python
* pytest
* Git
* GitHub
* GitHub Codespaces
* VS Code

## 🎯 Project Goals

The core project is now complete as a focused Python learning project.

Possible future enhancements include:

* Supporting additional log formats
* More detailed statistics and summaries
* More advanced filtering and searching
* JSON output
* Improved command-line argument handling
* More extensive automated testing

These are optional future improvements rather than requirements for the current project.

## 📚 Learning Focus

This project was developed as a practical way to learn Python programming, debugging, testing, and problem-solving.

Concepts practiced include:

* Variables and counters
* Conditional statements
* `if` / `elif` / `else`
* Nested `if` statements
* `for` loops
* String methods
* Lists and indexing
* File handling
* `with open()`
* f-strings
* `None` and optional values
* Command-line arguments with `sys.argv`
* `try` / `except`
* `FileNotFoundError`
* Functions with `def`
* Parameters and arguments
* Return values
* Variable scope
* Function calls
* Imports and modules
* `__name__ == '__main__'`
* Basic automated testing with `pytest`
* Assertions with `assert`
* Expected exceptions with `pytest.raises()`
* Git version control
* Git staging and reviewing changes

The project was intentionally built through small iterations rather than being designed as a large application from the beginning.

> [!NOTE]
> This project is primarily a learning exercise. The emphasis is on understanding the code, practicing problem-solving, debugging mistakes, and developing good development habits rather than simply producing a finished application.

## 📌 Project Status

✅ **Core project complete**

The analyzer accepts a log filename from the command line and optionally accepts a keyword to search for. It performs log-level analysis, counts recognized and unknown entries, calculates percentages, handles missing log files, and reports keyword matches.

The project also includes a small `pytest` test suite covering the reusable functions and expected error behavior.

The current implementation is intentionally simple and provides a foundation for future Python and IT-focused projects.
