from person import Person
from Book import Book


def main():
    book = Book()
    while True:
        print('Выбери действие: 1-Добавление записи/2 - Показать все записи/3-Удаление/4-Завершить работу: ')
        option = int(input('Действие: '))
        if option == 1:
            book.add_person(Person())
        elif option == 2:
            book.show_all()
        elif option == 3:
            i = int(input('Введите индекс(0,1,2...) человека для удаления: '))
            book.del_person(i)
        elif option == 4:
            print('Работа завершена!')
            break

main()