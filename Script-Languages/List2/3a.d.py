import sys
from utils import get_path_of_request


def is_image(value):
    image_extensions = ['gif', 'jpg', 'jpeg', 'xbm']
    return value in image_extensions


def find_ratio(lines):
    quantity = 0
    graphics = 0

    for line in lines:
        quantity += 1
        path = get_path_of_request(line)
        split_request = path.split('.')
        if len(split_request) > 1:
            extension = split_request[1].strip()
            if is_image(extension):
                graphics += 1

    return graphics / quantity


def find_ratio_of_graphics():
    ratio = find_ratio(sys.stdin)
    sys.stdin.close()

    ratio = round(ratio, 2)
    print(f'The ratio of graphics to all is: {ratio}')


if __name__ == '__main__':
    find_ratio_of_graphics()
