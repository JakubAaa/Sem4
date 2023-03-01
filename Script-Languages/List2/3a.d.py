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


def find_ratio_of_graphics():
    sum_of_all = 0
    graphics_sum = 0

    for line in sys.stdin:
        sum_of_all += 1
        path = get_path_of_request(line)
        split_request = path.split('.')
        if len(split_request) > 1:
            extension = split_request[1].strip()
            if is_gif(extension) or is_jpg(extension) or is_jpeg(extension) or is_xbm(extension):
                graphics_sum += 1

    ratio = graphics_sum / sum_of_all
    ratio = round(ratio, 2)
    print(f'The ratio of graphics to all is: {ratio}')


if __name__ == '__main__':
    find_ratio_of_graphics()
