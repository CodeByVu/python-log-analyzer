import argparse
import sys


def get_log_level(line):
    log_level = line.split()[0]
    return log_level


def keyword_matches(line, keyword):
    return keyword.lower() in line.lower()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('log_filename')
    parser.add_argument('--keyword')

    parser.add_argument(
        '--level',
        type=str.upper,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'UNKNOWN']
    )

    args = parser.parse_args()

    log_filename = args.log_filename
    keyword = args.keyword
    level_filter = args.level

    debug_count = 0
    info_count = 0
    warning_count = 0
    error_count = 0
    critical_count = 0
    unknown_count = 0
    match_count = 0

    try:
        with open(log_filename) as file:
            if keyword is None:
                print('No keyword provided. Skipping keyword search.')

            for line in file:
                line = line.strip()
                if line == '':
                    continue

                log_level = get_log_level(line)

                if log_level == 'DEBUG':
                    debug_count += 1

                elif log_level == 'INFO':
                    info_count += 1

                elif log_level == 'WARNING':
                    warning_count += 1

                elif log_level == 'ERROR':
                    error_count += 1

                elif log_level == 'CRITICAL':
                    critical_count += 1

                else:
                    unknown_count += 1

                if level_filter is not None:
                    if level_filter == 'UNKNOWN':
                        if log_level in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
                            continue

                    elif log_level != level_filter:
                        continue

                if keyword is not None:
                    if not keyword_matches(line, keyword):
                        continue

                if keyword is not None or level_filter is not None:
                    match_count += 1
                    print(f'MATCH #{match_count}:\n{line}')

    except FileNotFoundError:
        print('File not found')
        sys.exit(1)

    total_count = (
        debug_count
        + info_count
        + warning_count
        + error_count
        + critical_count
        + unknown_count
    )

    print(f'MATCHES: {match_count}')
    print(f'DEBUG: {debug_count}')
    print(f'INFO: {info_count}')
    print(f'WARNING: {warning_count}')
    print(f'ERROR: {error_count}')
    print(f'CRITICAL: {critical_count}')
    print(f'UNKNOWN: {unknown_count}')
    print(f'TOTAL: {total_count}')

    if total_count != 0:
        debug_percentage = debug_count / total_count * 100
        print(f'DEBUG PCT: {debug_percentage}%')
        info_percentage = info_count / total_count * 100
        print(f'INFO PCT: {info_percentage}%')
        warning_percentage = warning_count / total_count * 100
        print(f'WARNING PCT: {warning_percentage}%')
        error_percentage = error_count / total_count * 100
        print(f'ERROR PCT: {error_percentage}%')
        critical_percentage = critical_count / total_count * 100
        print(f'CRITICAL PCT: {critical_percentage}%')
        unknown_percentage = unknown_count / total_count * 100
        print(f'UNKNOWN PCT: {unknown_percentage}%')

if __name__ == '__main__':
    main()