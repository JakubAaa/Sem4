import sys
from utils import get_property_by_index, filter_and_print


def is_from_poland(line):
    host = get_property_by_index(line, 0)
    split_host = host.split('.')
    domain = split_host[-1]
    return domain == 'pl'


if __name__ == "__main__":
    filter_and_print(sys.stdin, is_from_poland)
