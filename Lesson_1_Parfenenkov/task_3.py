"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

str_1 = 'attribute'
str_2 = 'класс'
str_3 = 'функция'
str_4 = 'type'

lst = [str_1, str_2, str_3, str_4]

def str_to_b(str_in):
    try:
        str_1_out = bytes(str_in, encoding='ascii')
        print(type(str_in), str_1_out, type(str_1_out))
    except UnicodeEncodeError:
        print("There was an error encrypting...")


for el in lst:
    str_to_b(el)



