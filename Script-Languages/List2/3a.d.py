import sys
from utils import get_path_of_request


def is_gif(value):
    return value == 'gif'


def is_jpg(value):
    return value == 'jpg'


def is_jpeg(value):
    return value == 'jpeg'


def is_xbm(value):
    return value == 'xbm'


def find_ratio(lines):
    quantity = 0
    graphics = 0

    for line in lines:
        quantity += 1
        path = get_path_of_request(line)
        split_request = path.split('.')
        if len(split_request) > 1:
            extension = split_request[1].strip()
            if is_gif(extension) or is_jpg(extension) or is_jpeg(extension) or is_xbm(extension):
                graphics += 1

    return graphics / quantity


def find_ratio_of_graphics():
    ratio = find_ratio(sys.stdin)
    sys.stdin.close()

    ratio = round(ratio, 2)
    print(f'The ratio of graphics to all is: {ratio}')


if __name__ == '__main__':
    find_ratio_of_graphics()
