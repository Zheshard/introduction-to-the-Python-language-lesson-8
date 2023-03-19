import view

doc = "phonebook.txt"

# Чтение данных из документа:
def read_data(link_to_doc):
    with open(link_to_doc, "r", encoding='utf-8') as data:
        subscribers = (data.readlines())
        subscribers = [i.strip().split() for i in subscribers] #.split()
        data.close()
        return subscribers

# Перезаписать документ:
def write_data(link_to_doc, src_list):
    src_list = [(' '.join(i)) for i in src_list]
    with open(link_to_doc, "w", encoding='utf-8') as data:
        for i in range(len(src_list)-1):
            data.write(f"{src_list[i]}\n")
        data.write(f"{src_list[len(src_list)-1]}")
        data.close()

# Функция вывода результатов работы с файлом:
def print_res(output_list):
    if len(output_list) != 0:
        print('Список абонентов:')
        output_list = [f"{i+1} {' '.join(output_list[i])}" for i in range(len(output_list))] # собрать в строку данные абонента и добавить нумерацию
        output_list ='\n'.join(output_list) # собрать в один элемент всех абонентов с переносом каждого на новую строку
        print(output_list)
    else: view.print_not_found()

# Выбор варианта импорта данных:
def import_data():
    op_import = view.get_op_import()
    match op_import: 
        case '0':
            view.print_canceled() #Отмена
        case '1':
            return selective_import() # Поиск по имени или по фамилии
        case '2':
            return import_all() # Импорт всех
        case _:
            view.print_error()
            import_data()

# Функция поиска и импорта данных по имени или по фамилии, в зависимости от выбора пользователя:
def selective_import():
    search = view.get_name()
    subscribers = read_data(doc)
    res = {}
    for i in range(len(subscribers)):
        if search in subscribers[i]:
            res[i] = subscribers[i]
    print_res(list(res.values()))
    return res

# Функция импорта всех абонентов:
def import_all():
    res = read_data(doc)
    print_res(res)
    return res

# Добавить абонента в справочник:
def export_data():
    phone_list = list(read_data(doc))
    new_sub = view.get_export()
    if new_sub != '':
        with open(doc, "a", encoding='utf-8') as data:
            if phone_list == []: # проверка, является справочник пустым. если справочник пустой, то первый элемент добавляется без преноса строки
                data.write(f'{new_sub}')
            else:
                data.write(f'\n{new_sub}')
            data.close()

# Выбор варианта удаления данных
def delete_data():
    op_delete = view.get_op_delete()
    match op_delete: 
        case '0':
            view.print_canceled() #Отмена
        case '1':
            selective_delete() # Поиск по имени или по фамилии
        case '2':
            delete_all() # Удалить все
        case _:
            view.print_error()
            delete_data()

# Удалить выбранный элемент:
def selective_delete():
    subscribes = read_data(doc) # в переменную sub записывается все содержимое файла
    found_sub = selective_import() # Найти все элементы, удволетворяющие запросу пользователя (возвращается словарь элементов файла)
    num_str = 1
    if len(found_sub) > 1: # Если найденных элементов больше одного, то предлагается выбрать номер строки для удаления
        num_str = int(view.get_num_str())
    elif len(found_sub) == 0: return 0 
    deleted_elem = subscribes.pop(list(found_sub.keys())[num_str-1]) # из исходного списка удаляется абонент с вычисленным индексом
    print(f'{deleted_elem} удален')
    write_data(doc, subscribes) # список абонентов перезаписывается

# Удалить все элементы:
def delete_all():
    with open(doc, "w", encoding='utf-8') as data:
        data.write('')
        data.close()

# Имзенить данные:
def change_data():
    subscribes = read_data(doc) # в переменную sub записывается все содержимое файла
    found_sub = selective_import() # Найти все элементы, удволетворяющие запросу пользователя (возвращается словарь элементов файла)
    num_str = 1
    if len(found_sub) > 1: # Если найденных элементов больше одного, то предлагается выбрать номер строки для изменения
        num_str = int(view.get_num_str())
    print('Введите новые данные:')
    index = list(found_sub.keys())[num_str-1]
    subscribes[index] = view.get_export() # в исходном списке имзеняются данные абонента с вычисленным индексом
    subscribes[index] = subscribes[index].split()
    write_data(doc, subscribes)

# Отсортировать список абонентов в документе по имени либо фамилии, в зависимости от выбора пользователя:
def sorted():
    op_sort = int(view.get_op_sort()) # в переменную op_sort записывается результат выбора пользователя
    subscribes = read_data(doc)
    subscribes.sort(key=lambda i: i[op_sort - 1])
    write_data(doc, subscribes)