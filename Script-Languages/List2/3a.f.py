import sys
from utils import get_property_by_index


def is_from_22_to_6(line):
    date = get_property_by_index(line, 1)
    split_date = date.split(':')
    hour = int(split_date[1])
    return hour >= 22 or hour < 6


def print_only_between_22_6():
    for line in sys.stdin:
        if is_from_22_to_6(line):
            print(line.strip())

    sys.stdin.close()


if __name__ == "__main__":
    print_only_between_22_6()
