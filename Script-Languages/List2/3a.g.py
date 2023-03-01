import sys
import datetime
from utils import get_property_by_index


def is_from_friday(line):
    date = get_property_by_index(line, 1).split()[0]
    converted_date = datetime.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S')
    day_of_week = converted_date.weekday()
    return day_of_week == 4


def print_friday_requests():
    for line in sys.stdin:
        if is_from_friday(line):
            print(line.strip())

    sys.stdin.close()


if __name__ == "__main__":
    print_friday_requests()
