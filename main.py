from pprint import pprint

# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

'''
структура файла с рецептами:

Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения
'''

def get_shop_list_by_dishes(cook_book: dict, dishes: list, person_count: int) -> dict:
    ''' Задание 2. Функция получения списка ингралиентов. '''
    dict_ = {}
    for dish in dishes:
        for ingr_ in cook_book[dish]:
            dict_.setdefault(ingr_['ingredient_name'], {})
            dict_[ingr_['ingredient_name']]['measure'] = ingr_['measure']
            dict_[ingr_['ingredient_name']].setdefault('quantity', 0)
            dict_[ingr_['ingredient_name']]['quantity'] += ingr_['quantity'] * person_count
    return dict_

def readcookbook(filename):
    """ Задание 1. Читает файл с рецептами и записывает данные в словарь cook_book """
    with open(filename, encoding='utf-8') as f:
        cook_book = {}
        dish = f.readline().strip()
        while dish:
            cook_book.setdefault(dish, [])
            n = int(f.readline().strip())
            for i_ in range(n):
                _ = {}
                _['ingredient_name'], _['quantity'], _['measure'] = f.readline().split(' | ')
                _['ingredient_name'] = _['ingredient_name'].strip()
                _['quantity'] = int(_['quantity'].strip())
                _['measure'] = _['measure'].strip()
                cook_book[dish].append(_)
            f.readline()
            dish = f.readline().strip()
    return cook_book

def testcookbook():
    ''' Задания 1, 2. Демонстрирует выполнение 1 и 2 задания из домашней работы. '''

    filename = 'recipes.txt'
    cook_book = readcookbook(filename)

    print('#' * 30, ' Печать словаря cook_book - результата чтения файла ', '#' * 30)
    pprint(cook_book, sort_dicts=False)
    print()

    dishes = ['Омлет', 'Фахитос']
    dict_ = get_shop_list_by_dishes(cook_book, dishes, 10)
    print('#' * 30, ' Печать списка (в виде словаря) инградиентов для закупки ', '#' * 30)
    pprint(dict_, sort_dicts=False)

def readfiles(files):
    ''' Задание 3. Читает файлы из списка файлов files в виде списков.
    Каждый файл записывается в список где первый элемент имя файла
    второй элемент - количество строк в файле,
    остальные элементы - строки файла.
    Выдает результат в виде списка списков '''
    flists_ = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            flist_ = f.readlines()
            flist_ = [_.rstrip('\n') for _ in flist_]
            flist_ = [f.name, len(flist_)] + flist_
        flists_.append(flist_)
    return flists_

def writefiles(file_list, filename, sort=True):
    """ Задание 3. Получает список данных для записи в файл в виде писка списков,
    сортирует его по второму элементу каждого списка (там должно быть
    записано число строк файла) и записываеи в файл. """
    if sort:
        file_list_ = sorted(file_list, key=lambda x: x[1])
    else:
        file_list_ = file_list[:]

    with open(filename, 'w', encoding='utf-8') as f:
        for flist_ in file_list_:
            print(*flist_, file=f, sep='\n')

def testjoinfiles():
    """ Задание 3. Демонтрация работы функций. """
    files = ['1.txt', '2.txt', '3.txt']
    file_list = readfiles(files)

    print(f'------------------------------ список -----------------------------------')
    [print(i) for i in file_list]
    print(f'--------------------- ---------------------------------------------------')
    writefiles(file_list, 'result.txt')

def main():

    # Задание 1, 2
    testcookbook()
    # Задание 3
    testjoinfiles()

if __name__ == '__main__':
    main()