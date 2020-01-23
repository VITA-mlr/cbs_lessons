import shelve


def write(filename, short, long):
    with shelve.open(filename, 'c') as file:
        file[short] = long
        while input('If you want continuation you must press 1 - ') == '1':
            long = input('Input long url - ')
            short = input('Input short url - ')
            file[short] = long


def read(filename, key):
    with shelve.open(filename, 'r') as file:
        url = file.get(key, "Undefined")

    return url
