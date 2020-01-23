"""Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.
"""


class MyExсeption(Exception):
    pass


if __name__ == "__main__":
    try:
        a = int(input('a = '))
        if a == 5:
            raise MyExсeption("Це мій вийняток!!!")
    except MyExсeption as e:
        print("Error: ", e)
    finally:
        exit(1)

