import sys
from utils import get_property_by_index, get_path_of_request


def find_path_of_the_biggest_request():
    max_size = 0
    path_of_max = ''

    for line in sys.stdin:
        size = get_property_by_index(line, 4)
        if size != '-':
            size = int(size)
            if size > max_size:
                max_size = size
                path_of_max = get_path_of_request(line)

    print(f'Path of the biggest request: {path_of_max} size: {max_size}')


if __name__ == '__main__':
    find_path_of_the_biggest_request()
