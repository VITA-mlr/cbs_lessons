"""
Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
указывая параметры
"""


def main():
    long_name = input('Input long url - ')
    short_name = input('Input short url - ')

    url = dict.fromkeys(short_name, long_name)
    # url[short_name]=long_name

    key = input('Input short url key - ')
    if key in url:
        print(url[key])
    else:
        print('Uncorectly short name!!!!')


if __name__ == '__main__':
    main()
