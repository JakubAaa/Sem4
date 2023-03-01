import sys
from utils import get_property_by_index


def count_sum_of_sizes():
    counter = 0

    for line in sys.stdin:
        value = get_property_by_index(line, 4)
        if value == '-':
            value = 0

        counter += int(value)

    counter = counter / (1024 ** 3)
    counter = round(counter, 2)
    print(f'Sum of sizes: {counter}Gb')


if __name__ == '__main__':
    count_sum_of_sizes()
