#!/usr/bin/env python3
import sys

lines_processed = 0
total_file_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        line = line.strip()
        elements = line.split()

        # Skip lines with incorrect format
        if len(elements) != 9:
            continue

        ip_address = elements[0]
        status_code = elements[8]
        file_size = int(elements[7])

        # Update metrics
        lines_processed += 1
        total_file_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print(f"File size: {total_file_size}")
            sorted_status_codes = sorted(status_codes.items(), key=lambda x: int(x[0]))
            for code, count in sorted_status_codes:
                print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    pass

# Print final statistics
print(f"File size: {total_file_size}")
sorted_status_codes = sorted(status_codes.items(), key=lambda x: int(x[0]))
for code, count in sorted_status_codes:
    print(f"{code}: {count}")

