import sys


def print_all():
    for line in sys.stdin:
        print(line)

    sys.stdin.close()


if __name__ == "__main__":
    print_all()
