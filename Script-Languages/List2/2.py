import sys
from utils import get_property_by_index


def print_all():
    for line in sys.stdin:
        get_property_by_index(line, 1)

    sys.stdin.close()
