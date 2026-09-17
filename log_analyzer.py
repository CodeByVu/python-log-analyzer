import sys

if len(sys.argv) >= 2:
    log_filename = sys.argv[1]
else:
    print('Log file not detected, please provide one')
    sys.exit()

info_count = 0
warning_count = 0
error_count = 0 
debug_count = 0
unknown_count = 0

with open(log_filename) as file:
    for line in file:
        log_level = line.split()[0]

        if log_level == 'INFO':
            info_count += 1

        elif log_level == 'WARNING':
            warning_count += 1

        elif log_level == 'ERROR':
            error_count += 1

        elif log_level == 'DEBUG':
            debug_count += 1

        else:
            unknown_count += 1

total_count = info_count + warning_count + error_count + debug_count + unknown_count

print(f'INFO: {info_count}')
print(f'WARNING: {warning_count}')
print(f'ERROR: {error_count}')
print(f'DEBUG: {debug_count}')
print(f'UNKNOWN: {unknown_count}')
print(f'TOTAL: {total_count}')

if total_count == 0:
    print(f'TOTAL: {total_count}')
else:
    info_percentage = info_count / total_count * 100
    print(f'INFO PCT: {info_percentage}%')
    warning_percentage = warning_count / total_count * 100
    print(f'WARNING PCT: {warning_percentage}%')
    error_percentage = error_count / total_count * 100
    print(f'ERROR PCT: {error_percentage}%')
    debug_percentage = debug_count / total_count * 100
    print(f'DEBUG PCT: {debug_percentage}%')
    unknown_percentage = unknown_count / total_count * 100
    print(f'UNKNOWN PCT: {unknown_percentage}%')
