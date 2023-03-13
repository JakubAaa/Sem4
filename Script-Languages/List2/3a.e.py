import sys
from utils import get_property_by_index, filter_and_print


def is_200(line):
    code = get_property_by_index(line, 3)
    return code == '200'


def print_all_with_code_200():
    filter_and_print(sys.stdin, is_200)


if __name__ == "__main__":
    print_all_with_code_200()
