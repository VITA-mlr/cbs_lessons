"""
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
отрицательную степень.
"""


class MyException(Exception):
    pass


def calcul():
    print('Введіть вираз, що потрібно обчислити:')
    a = int(input('a = '))
    action = input('Яку дію виконати? ')
    b = int(input('b = '))
    if action == "+":
        return a+b
    elif action == "-":
        return a-b
    elif action == "*":
        return a*b
    elif action == "/":
        return a/b
    elif action == "**":
        return a**b
    elif action != "+" or action != "-" or action != "*" or action != "/" or action !="**":
        raise MyException


def main():
    while 1:
        try:
            print("Результат - ", calcul())
        except ValueError:
            print("Дані повині бути числові.")
        except ZeroDivisionError:
            print("Ділення на нуль неможливе")
        except MyException:
            print('Введіть, будь-ласка, арифметичну дію коректно!')
        except Exception:
            print('От і помилочка знову.')
        finally:
            if input('Для закриття програми введіть 0 ') == '0':
                break


if __name__ == "__main__":
    main()
