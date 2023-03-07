import re


def process_line(line):
    try:
        properties = re.match(r"(.+) - - \[(.+) \"(.+)\" (.+) (.+)", line)
        return [properties[1], properties[2], properties[3], properties[4], properties[5]]
    except Exception:
        raise Exception('Wrong line!')


def get_property_by_index(line, index):
    split_line = process_line(line)
    return split_line[index]


def get_path_of_request(line):
    request = get_property_by_index(line, 2)
    split_request = request.split()

    if len(split_request) < 2:
        return request

    return split_request[1].strip()


def filter_and_print(file, filter_function):
    for line in file:
        if filter_function(line):
            print(line.strip())
    file.close()
