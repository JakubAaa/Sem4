import sys
from utils import get_property_by_index


def count(lines):
    c200 = 0
    c302 = 0
    c404 = 0

    for line in lines:
        code = get_property_by_index(line, 3)
        if code == '200':
            c200 += 1
        if code == '302':
            c302 += 1
        if code == '404':
            c404 += 1
    return [c200, c302, c404]


def count_requests_by_code():
    result = count(sys.stdin)
    sys.stdin.close()

    counter200 = result[0]
    counter302 = result[1]
    counter404 = result[2]

    print(f'Number of: 200={counter200}, 302={counter302}, 404={counter404}')


if __name__ == '__main__':
    count_requests_by_code()
