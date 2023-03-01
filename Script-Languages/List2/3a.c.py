import sys
from utils import get_property_by_index, get_path_of_request


def find_path_and_size(lines):
    size = 0
    path = ''

    for line in lines:
        value = get_property_by_index(line, 4)
        if value != '-':
            value = int(value)
            if value > size:
                size = value
                path = get_path_of_request(line)
    return [path, size]


def find_path_of_the_biggest_request():
    result = find_path_and_size(sys.stdin)
    sys.stdin.close()

    path_of_max = result[0]
    max_size = result[1]
    print(f'Path of the biggest request: {path_of_max}, size: {max_size}')


if __name__ == '__main__':
    find_path_of_the_biggest_request()
