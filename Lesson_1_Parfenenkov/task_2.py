"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

str_1 = 'class'
str_2 = 'function'
str_3 = 'method'

def str_to_b(str_in):
    str_1_out = bytes(str_in, encoding='utf-8')
    print(type(str_1))
    print(str_1_out)
    print(type(str_1_out))

str_to_b(str_1)
str_to_b(str_2)
str_to_b(str_3)

