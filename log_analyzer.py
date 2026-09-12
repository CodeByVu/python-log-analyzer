info_count = 0
warning_count = 0
error_count = 0 
debug_count = 0

with open('app.log') as file:
    for line in file:
        if 'INFO' in line:
            info_count += 1
            
        if 'WARNING' in line:
            warning_count += 1

        if 'ERROR' in line:
            error_count += 1

        if 'DEBUG' in line:
            debug_count += 1

total_count = info_count + warning_count + error_count + debug_count

print(f'INFO: {info_count}')
print(f'WARNING: {warning_count}')
print(f'ERROR: {error_count}')
print(f'DEBUG: {debug_count}')
print(f'TOTAL: {total_count}')

if total_count == 0:
    print('total_count is 0')
else:
    info_percentage = info_count / total_count * 100
    print(f'INFO PCT: {info_percentage}%')
    warning_percentage = warning_count / total_count * 100
    print(f'WARNING PCT: {warning_percentage}%')
    error_percentage = error_count / total_count * 100
    print(f'ERROR PCT: {error_percentage}%')
    debug_percentage = debug_count / total_count * 100
    print(f'DEBUG PCT: {debug_percentage}%')






