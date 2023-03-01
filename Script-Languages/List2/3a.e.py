import sys
from utils import get_property_by_index


def is_200(line):
    code = get_property_by_index(line, 3)
    return code == '200'


def print_all_with_code_200():
    for line in sys.stdin:
        if is_200(line):
            print(line.strip())

    sys.stdin.close()


if __name__ == "__main__":
    print_all_with_code_200()
