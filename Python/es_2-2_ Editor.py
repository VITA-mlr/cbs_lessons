""""
Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
edit_document выводит на экран информацию о том, что редактирование документов недоступно для
бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
иначе Editor. Вызовите методы просмотра и редактирования документов.
"""


class Editor:
    def __init__(self):
        print('Екземпляр класу Editor створений')

    def view_document(self):
        print('Метод - показує документ')

    def edit_document(self):
        print('Pедагування документів недоступне для безкошмовної версії.')


class ProEditor(Editor):

    def __init__(self):
        print('Екземпляр класу ProEditor створений')

    def edit_document(self):
        print('Редагування доступне')


def main():
    obj_Editor = Editor()
    obj_Editor.view_document()
    obj_Editor.edit_document()

    if input('Введите с клавиатуры лицензионный ключ - ') == '123':
        obj_ProEditor = ProEditor()
    else:
        obj_ProEditor = Editor()

    obj_ProEditor.view_document()
    obj_ProEditor.edit_document()


if __name__ == "__main__":
    main()
