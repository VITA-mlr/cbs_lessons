"""
Напишите функцию-генератор для получения n первых простых чисел.
"""


def simple(size, sequence):
    for el in range(2, size*size):
        for j in sequence:
            if el % j == 0:
                break
            else:
                if len(sequence) < size:
                    yield el
                    break


if __name__ == "__main__":
    l1 = [2]

    for i in simple(int(input('N= ')), l1):
        l1.append(i)

    print(l1)
