def url_dict(short, long):
    url = dict.fromkeys(short, long)
    return url


def url_key(url, key):
    if key in url:
        print(url[key])
    else:
        print('Uncorectly short name!!!!')
