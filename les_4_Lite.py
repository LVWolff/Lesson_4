
import random

def f(list_name, n):
    """
    генерирует новый список имен
    """
    n_list = []
    for i in range(n):
        n_list.append(random.choice(list_name))

    return n_list

def f_2(list_name, in_ind = 0):
    """
    выводит часто встречающееся у входящего списка имен
    """
    set_names = list(set(list_name))
    dict_names = {}
    list_count = []
    for name in set_names:
        count = list_name.count(name)
        dict_names.update([(count, name)])

    dict_key = dict_names.keys()
    new_list_count = sorted(dict_key, reverse=True)
    return dict_names[new_list_count[in_ind]]

def f_3(list_name):
    """
     функцию вывода самой редкой буквы, с которого начинаются имя
    :return: имя буквы
    """
    list_letter = list(map(lambda x: x[0], list_name))

    # воспользуемся уже готовой функции получения самого распространненого имени, только передадим туда
    # список букв и возьмем последний элемент после сортировки

    return f_2(list_letter, -1)

list_name = ['Ivan', 'Sergey', 'Dmitriy', 'John', 'Mike', 'Elena', 'Irina', 'Maria', 'Oleg']
n = random.randint(1, 51)
new_list = f(list_name, n)
print('n =', n, '\nсписок имен:', new_list)
print('Самое часто встречающееся имя:', f_2(new_list))
print('Самая редкая буква с которой начинается имя: ', f_3(new_list))