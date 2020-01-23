"""
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f' Назва - {self.title}\n Автор - {self.author}'

    def display(self):
        print(self)


class Reviews:
    def __init__(self, book):
        self.book = book
        self.book.listReviews = []

    def review(self):
        self.review = input(f'Залиште ваш відгук по книзі:\n{self.book}\n')
        self.book.listReviews.append(self.review)

    def display(self):
        print(f'\n{self.book}\n Відгуки -  {self.book.listReviews}')

    def opinion(self):
        self.op = input('\nОпишіть що думаєте про цей відгук або дайте йому оцінку(+ чи -) - ')
        self.op_int = 0
        self.op_str = []
        if self.op == '+':
            self.op_int += 1
            print(f'Відгук сподобався {self.op_int} раз!')
        elif self.op == '-':
            self.op_int += 1
            print(f'Відгук не сподобався {self.op_int} раз!')
        else:
            self.op_str.append(self.op)
            print(f'Ваш відгук - {self.op_str}')


def main():
    book1 = Book('Марк Лутс', 'Вивчаємо Python')
    book2 = Book('Олестад Норман', 'Безума від шторму')
    book3 = Book('Всеволод Нестайко', 'Тереодори з Васюківки')

    review_b2 = Reviews(book2)

    review_b2.review()
    review_b2.display()
    review_b2.opinion()


if __name__ == '__main__':
    main()
