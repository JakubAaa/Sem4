import sys
from utils import get_property_by_index, filter_and_print


def is_from_22_to_6(line):
    date = get_property_by_index(line, 1)
    split_date = date.split(':')
    hour = int(split_date[1])
    return hour >= 22 or hour < 6


def print_only_between_22_6():
    filter_and_print(sys.stdin, is_from_22_to_6)


if __name__ == "__main__":
    print_only_between_22_6()
