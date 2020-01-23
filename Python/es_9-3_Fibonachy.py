"""
Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в
последовательности только чётные числа.
"""


def positive(fn):
    def decorator(*args):
        fibo = fn(*args)
        rfibo = []
        for el in fibo:
            if el % 2 == 0:
                rfibo.append(el)
        return rfibo
    return decorator


@positive
def fibo(x, previous=1, now=1):
    for i in range(x):
        if i == 0 or i == 1:
            yield 1
            i += 1
        else:
            if x > i:
                f_current = now + previous
                yield f_current
                previous = now
                now = f_current
                i += 1


if __name__ == "__main__":

    print("\nfibo positive :", list(fibo(10)))
