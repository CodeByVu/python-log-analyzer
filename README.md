# 🐍 Python Log Analyzer

A Python command-line utility for analyzing text-based log files, summarizing log-level statistics, and investigating entries through keyword and severity-level filtering.

This project was developed incrementally as a hands-on Python and IT learning project, focusing on practical programming, troubleshooting concepts, automated testing, and version control.

## ✨ Features

- Counts `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` log entries.
- Identifies the log level from the first word of each line.
- Categorizes unrecognized log levels as `UNKNOWN`.
- Calculates the percentage of entries in each category.
- Reports the total number of nonblank entries analyzed.
- Reads log files line by line and skips blank lines.
- Supports optional keyword searching using case-insensitive substring matching.
- Supports log-level filtering through the `--level` command-line option.
- Accepts case-insensitive log-level filter input.
- Supports combining keyword and log-level filters.
- Displays and numbers matching entries.
- Reports the total number of matching entries.
- Calculates statistics across the entire file, regardless of active filters.
- Uses `argparse` for command-line argument handling and validation.
- Handles missing log files with `FileNotFoundError`.
- Includes automated tests using `pytest`.

## 💻 Getting Started

### Requirements

- Python 3
- `pytest` (required for running automated tests)

The application uses Python's standard library and does not require additional runtime packages.

### Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install pytest:

```bash
python -m pip install pytest
```

## 🚀 Usage

The program requires a log filename and optionally accepts a keyword, a log-level filter, or both.

### Analyze a log file

```bash
python log_analyzer.py sample.log
```

Without filters, the analyzer reports statistics for the entire file without displaying individual log entries.

### Search by keyword

```bash
python log_analyzer.py sample.log --keyword database
```

Keyword searches are case-insensitive. The supplied keyword can appear anywhere within a log entry.

### Filter by log level

```bash
python log_analyzer.py sample.log --level ERROR
```

Supported log-level filters:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`
- `UNKNOWN`

Log-level filter input is case-insensitive. For example, `--level error` works the same as `--level ERROR`.

`UNKNOWN` matches entries whose first word is not one of the five recognized severity levels.

### Combine keyword and log-level filters

```bash
python log_analyzer.py sample.log --keyword database --level ERROR
```

When both filters are supplied, an entry must satisfy both conditions to be displayed.

Statistics continue to reflect every nonblank entry in the file, even when filters are active.

## 📄 Sample Log File

The following sample can be saved as `sample.log` in the project directory:

```text
INFO Application started
DEBUG Configuration loaded
WARNING Database response delayed
ERROR Database connection failed
ERROR Authentication failed
CRITICAL System failure
NOTICE Cache refresh completed
```

This sample includes all five recognized severity levels and an unrecognized level for testing `UNKNOWN` classification.

## 📊 Example Output

Running the combined filtering command:

```bash
python log_analyzer.py sample.log --keyword database --level ERROR
```

Produces:

```text
MATCH #1:
ERROR Database connection failed
MATCHES: 1
DEBUG: 1
INFO: 1
WARNING: 1
ERROR: 2
CRITICAL: 1
UNKNOWN: 1
TOTAL: 7
DEBUG PCT: 14.285714285714285%
INFO PCT: 14.285714285714285%
WARNING PCT: 14.285714285714285%
ERROR PCT: 28.57142857142857%
CRITICAL PCT: 14.285714285714285%
UNKNOWN PCT: 14.285714285714285%
```

Only entries satisfying both filters are displayed, while statistics cover the entire file.

## 🧪 Automated Tests

The project uses `pytest` to verify individual functions, command-line argument handling, filtering behavior, error handling, and statistics.

Run the complete test suite with:

```bash
python -m pytest
```

The V2 test suite contains 18 automated tests.

## ⚠️ Current Limitations

The analyzer intentionally uses a simple text-based log format.

- The log level must be the first word of each nonblank line.
- Recognized log levels in the file must use uppercase names: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- Other first-word values are categorized as `UNKNOWN`.
- Keyword searches use case-insensitive substring matching, so a keyword may match part of a larger word.
- The analyzer is designed for basic text-based log investigation rather than structured log formats or production monitoring.
- Missing files are explicitly handled; other file-related errors are not currently handled separately.

These limitations leave room for future improvements without unnecessarily complicating the current implementation.

## 🛠️ Technologies

- Python
- `argparse`
- `pytest`
- Git
- GitHub
- GitHub Codespaces
- Visual Studio Code

## 📚 Version History

### V2

- Added command-line argument parsing using `argparse`.
- Added case-insensitive keyword searching.
- Added log-level filtering with case-insensitive command-line input.
- Added `CRITICAL` log-level classification and statistics.
- Added filtering for unrecognized (`UNKNOWN`) log entries.
- Added support for combining keyword and log-level filters.
- Updated match counting and reporting.
- Expanded automated test coverage to 18 tests.

### V1

- Implemented the initial command-line log analyzer.
- Added log-level counting and percentage reporting.
- Added keyword searching and match reporting.
- Implemented line-by-line file processing and blank-line skipping.
- Added missing-file error handling.
- Introduced reusable functions and automated tests.

## 🎯 Project Goals

This project focuses on developing practical Python skills through incremental development.

Areas of experience include:

- File handling and text processing.
- Conditional logic, loops, and functions.
- Command-line interfaces and argument validation.
- Exception handling.
- Boolean logic and filtering.
- Automated testing and debugging.
- Git version control and incremental development.

Future enhancements may explore additional log formats, output customization, and more advanced analysis capabilities.

---

**Project Status: V2 feature set complete.**