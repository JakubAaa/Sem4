import sys
from utils import get_property_by_index


def calculate_sum_in_gb(lines):
    counter = 0

    for line in lines:
        value = get_property_by_index(line, 4)
        if value != '-':
            counter += int(value)

    return counter / (1024 ** 3)


def count_sum_of_sizes():
    counter = calculate_sum_in_gb(sys.stdin)
    sys.stdin.close()

    counter = round(counter, 2)
    print(f'Sum of sizes: {counter}Gb')


if __name__ == '__main__':
    count_sum_of_sizes()
