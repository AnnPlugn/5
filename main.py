import warnings
import universal
import db

warnings.filterwarnings("ignore")


def append_to_list():
    list_1 = input("enter: ").split()
    a = input('a: ')
    list_1.append(a)
    print(list_1)
    db.save_result('listappend: ', list_1)
    return


def list_extend():
    list_1 = input("enter: ").split()
    list_2 = input("enter: ").split()
    list_1.extend(list_2)
    print(list_1)
    db.save_result('listextend: ', list_1)
    return


def list_reverse():
    list_1 = input("enter: ").split()
    list_1.reverse()
    print(list_1)
    db.save_result('listreverse: ', list_1)
    return


def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Добавить элемент в список, результат сохранить в MySQL.
3. Соединить списки, результат сохранить в MySQL.
4. Перевернуть список, результат сохранить в MySQL.
5. Сохранить все данные из MySQL в Excel.
6. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, append_to_list, list_extend, list_reverse,
                            db.save_db_to_xlxs)
    return


if __name__ == '__main__':
    main()
