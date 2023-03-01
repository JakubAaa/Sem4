import sys
from utils import get_property_by_index


def count_requests_by_code():
    counter200 = 0
    counter302 = 0
    counter404 = 0

    for line in sys.stdin:
        code = get_property_by_index(line, 3)
        if code == '200':
            counter200 += 1
        if code == '302':
            counter302 += 1
        if code == '404':
            counter404 += 1

    print(f'Number of: 200={counter200}, 302={counter302}, 404={counter404}')


if __name__ == '__main__':
    count_requests_by_code()
