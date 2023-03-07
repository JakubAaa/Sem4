import sys
import datetime
from utils import get_property_by_index, filter_and_print


def is_from_friday(line):
    date = get_property_by_index(line, 1).split()[0]
    converted_date = datetime.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S')
    day_of_week = converted_date.weekday()
    return day_of_week == 4


if __name__ == "__main__":
    filter_and_print(sys.stdin, is_from_friday)
