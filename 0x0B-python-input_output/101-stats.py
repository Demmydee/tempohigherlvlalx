#!/usr/bin/python3
"""
	A script that reads stdin line by line and computes metrics"""


def print_stats(file_size, status_code):
    """Prints total metrics.
    Args:
        file_size : Total read file size.
        status_code : Total count of status codes.
    """
    print("File size: {}".format(file_size))
    for i in sorted(status_code):
        print("{}: {}".format(i, status_code[i]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_code = {}
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for j in sys.stdin:
            if c == 10:
                print_stats(file_size, status_code)
                c = 1
            else:
                c += 1
            j = j.split()
            try:
                file_size += int(j[-1])
            except (IndexError, ValueError):
                pass
            try:
                if j[-2] in status_codes:
                    if status_code.get(j[-2], -1) == -1:
                        status_code[j[-2]] = 1
                    else:
                        status_code[j[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_code)

    except KeyboardInterrupt:
        print_stats(file_size, status_code)
        raise
