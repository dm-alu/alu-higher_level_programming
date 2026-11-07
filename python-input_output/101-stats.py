#!/usr/bin/python3
"""Read log lines on stdin and print metrics every ten lines."""
import sys


def print_stats(total, codes):
    """Print the total file size and the number of lines per status code."""
    print("File size: {}".format(total))
    for code in sorted(codes):
        print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
    total = 0
    count = 0
    codes = {}
    valid = ("200", "301", "400", "401", "403", "404", "405", "500")
    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                size = int(parts[-1])
                code = parts[-2]
                total += size
                if code in valid:
                    codes[code] = codes.get(code, 0) + 1
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(total, codes)
        if count % 10 != 0:
            print_stats(total, codes)
    except KeyboardInterrupt:
        print_stats(total, codes)
        raise
