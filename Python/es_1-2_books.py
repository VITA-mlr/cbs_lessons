"""
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
равенство и неравенство, методы __repr__ и __str__.
"""


class Book:
    def __init__(self, author, title, year, publishing_house, genre):
        self.author = author
        self.title = title
        self.year = year
        self.publishing_house = publishing_house
        self.genre = genre
        self.list_reviews = []

    def add_review(self):
        print(f'\nЗалиште ваш відгук по книзі - {self}\n')
        rev = input('Відгук: ')
        evaluation = input('Оцінка: ')
        self.list_reviews.append(Review(rev, evaluation))

    def __repr__(self):
        return '%s, %s, %i, %s, %s' % (self.author, self.title, self.year, self.publishing_house, self.genre)

    def __str__(self):
        if len(self.list_reviews) == 0:
            return '%s, %s, %i, %s, %s' % (self.author, self.title, self.year, self.publishing_house, self.genre)
        else:
            return '%s, %s, %i, %s, %s, %s' % (self.author, self.title, self.year, self.publishing_house, self.genre,
                                               self.list_reviews)

    def __eq__(self, other):
        print('Function_eq')
        return self.author == other.author and self.title == other.title and self.year == other.year and \
               self.publishing_house == other.publishing_house and self.genre == other.genre


def main():
    book1 = Book('Mark Lutc', 'Learning Python', 2011, 'Simvol-Plyus', 'studing')
    book2 = Book('Ollestad Norman', 'Crazy for the Storm', 2014, 'Exmo', 'biographical')
    book3 = Book('Vsevolod Nestayko', 'Tereodors from Vasyukivka', 2004, 'A-ba-ba-ga-la-ma-ga', 'children')
    book4 = Book('Vsevolod Nestayko', 'Newest adventures of the hedgehog Kolka Klyuchki and the bunny Spi Vukhanya',
                 2016, 'A-ba-ba-ga-la-ma-ga', 'children')

    my_book = Book('Mark Lutc', 'Learning Python', 2011, 'Simvol-Plyus', 'studing')

    if book1 == my_book:
        print('Книги - однакові!!')
    else:
        print('Книги - не однакові!!!')

    if book3.author == book4.author:
        print('Книги одного автора.')
    else:
        print('Книги різних авторів.')

    if book2.publishing_house == book4.publishing_house:
        print('Книги одного видавництва.')
    else:
        print('Книги різних видавництв.')


if __name__ == '__main__':
    main()
