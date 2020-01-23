"""
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
после заданного года.
"""


class Employee:
    def __init__(self, name, last_name, section, since_year):

        self.name = name
        if self.name.isalpha() == False:
            raise Exception('імені')

        self.last_name = last_name
        if self.last_name.isalpha() == False:
            raise Exception('прізвища')

        self.section = section
        if self.section.isalnum() == False:
            raise ValueError('відділу')

        self.since_year = since_year
        if self.since_year.isdigit() == False:
            raise ValueError('poку прийняття на роботу')

    def __repr(self):
        return '[%s, %s, %s, %s]' % (self.name, self.last_name, self.section, self.since_year)

    def __str__(self):
        return f"\nІм'я працівника - {self.name}" \
               f"\nПрізвище прцівника - {self.last_name}" \
               f"\nВідділ - {self.section}" \
               f"\nРік прибуття на роботу - {self.since_year}"

    def __eq__(self, other):
        print('Function_eq')
        return self.name == other.name or self.last_name == other.last_name or self.section == other.section or\
               self.since_year == other.since_year


def main():
    listEmployee = []

    menu = 1

    while menu == 1:
        name = input("\nIм'я - ")
        last_name = input("Прізище - ")
        section = input("Відділ - ")
        since_year = input("З якого року працює - ")
        try:
            employee = Employee(name, last_name, section, since_year)
        except Exception as ver:
            print('Введіть коректні дані ', ver)

        listEmployee.append(employee)
        menu = int(input('Натисніть 1, якщо хочете розширити список працівників, або 2 для іншої операції '))
    year = input('\nВведіть потрібний Вам рік ')

    for employee in listEmployee:
        if employee.since_year <= year:
            print(employee)


if __name__ == "__main__":
    main()
