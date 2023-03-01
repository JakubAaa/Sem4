import sys
from utils import get_property_by_index


def is_from_poland(line):
    host = get_property_by_index(line, 0)
    split_host = host.split('.')
    domain = split_host[-1]
    return domain == 'pl'


def print_from_poland():
    for line in sys.stdin:
        if is_from_poland(line):
            print(line.strip())

    sys.stdin.close()


if __name__ == "__main__":
    print_from_poland()
