#!/usr/bin/python3
"""
Module 101-stats
"""

import sys
def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    try:
        for i, line in enumerate(sys.stdin, 1):
            data = line.split()
            if len(data) > 2:
                total_size += int(data[-1])
                code = int(data[-2])
                if code in status_codes:
                    status_codes[code] += 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
