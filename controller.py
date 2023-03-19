import view
import database


def main():
    match view.get_op():
        case '0' | '' | ' ':
            view.print_completed() # Заврешение работы
        case '1':
            database.import_data() # Импорт данных
            next_action()
        case '2':
            database.export_data() # Внесение данных в файл
            next_action()
        case '3':
            database.delete_data() # Удаление данных
            next_action()
        case '4':
            database.change_data() # Изменение данных
            next_action()
        case '5':
            database.sorted() # Сортировка справочника
            next_action()
        case _:
            view.print_error() # Недопустимое значение
            main()

# Запрос на продолжение, либо завершение работы:
def next_action():
    if view.get_next_action() != '0':
        main()
    else: view.print_completed()

if __name__ == "__main__":
    main()