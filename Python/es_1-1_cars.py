"""
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
"""


class Car:
    def __init__(self, brand, cab, color, engine_capacity):
        self.brand = brand
        self.cab = cab
        self.color = color
        self.engine_capacity = engine_capacity

    def __repr__(self):
        return '(%s, %s, %s, %f)' % (self.brand, self.cab, self.color, self.engine_capacity)


class AutoShop:
    def __init__(self):
        self.listCars = []

    def sell(self, car):
        print('Вітаємо з успішною продажею автомобіля {}'.format(car))
        self.listCars.pop(self.listCars.index(car))
        return(self.listCars)


bmw = Car('BMW', 'sedan', 'blak', 3)
cevro = Car('Chevrolet', 'crossover', 'white', 5)
ford = Car('Ford', 'cabriolet', 'gray', 1.5)


shop = AutoShop()

shop.listCars.append(bmw)
shop.listCars.append(cevro)
shop.listCars.append(ford)

print(shop.sell(bmw))
