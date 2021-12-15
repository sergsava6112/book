from person import Person



def main():
    while True:
        print('Выбери действие: 1-Добавление/2 - Показать все/3-Удаление всего и вся/4 - Завершить работу программы: ')
        option = int(input('Действие: '))
        if option == 1:
            with open('adress_book_1.txt', 'a') as file:
                file.write(str(Person()))
                file.write(str('\n'))
        elif option == 2:
            with open('adress_book_1.txt', 'r') as file:
                print(file.read())

        elif option == 3:
                with open('adress_book_1.txt', 'w') as file:
                    file.write(str('\n'))
                print('Все записи удалены!')

        elif option == 4:
            print('Работа завершена!')
            break

main()