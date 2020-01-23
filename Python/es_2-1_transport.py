"""
Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве.
"""


class Transports:
    def __init__(self,
                 doors,
                 rings,
                 seatings):

        self.doors = doors
        self.rings = rings
        self.seatings = seatings

    def __repr__(self):
        print('Hello')
        return '%i, %i, %i,' % (self.doors,
                                self.rings,
                                self.seatings)

    def __str__(self):
        return 'В мене є: {} колеса, {} двереці, {} сидячих місць'.format(self.doors,
                                                                          self.rings,
                                                                          self.seatings)

    def display(self):
        print(self)


class Planes(Transports):
    def __init__(self,
                 doors,
                 rings,
                 seatings,
                 wings):
        super().__init__(doors,
                         rings,
                         seatings)
        self.wings = wings

    def __str__(self):
        return 'В мене є: {} колеса, {} дверці, {} сидячих місць, {} крила'.format(self.doors,
                                                                                   self.rings,
                                                                                   self.seatings,
                                                                                   self.wings)


class Cars(Transports):
    def __init__(self,
                 doors,
                 rings,
                 seatings):
        super().__init__(doors,
                         rings,
                         seatings)


class Trucks(Cars):
    def __init__(self,
                 doors,
                 rings,
                 seatings,
                 cab):
        super().__init__(doors,
                         rings,
                         seatings)
        self.cab = cab

    def __str__(self):
        return 'В мене є: {} колеса, {} дверці, {} сидячих місць, {} кузово'.format(self.doors,
                                                                                    self.rings,
                                                                                    self.seatings,
                                                                                    self.cab)


if __name__ == '__main__':

    plane = Planes(1, 32, 110, 2)
    car = Cars(4, 4, 5)
    truck = Trucks(2, 6, 2, 1)

    car.display()
    plane.display()
    truck.display()
