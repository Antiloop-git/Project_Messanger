"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

str_1 = 'разработка'
str_2 = 'администрирование'
str_3 = 'protocol'
str_4 = 'standard'

lst = [str_1, str_2, str_3, str_4]

def str_to_b(str_in):
    try:
        str_out = str_in.encode(encoding='utf-8')
        print(type(str_in), str_out, type(str_out))

        str_out_str = str_out.decode(encoding='utf-8')
        print(str_out_str)

    except UnicodeEncodeError:
        print("There was an error encrypting...")



for el in lst:
    str_to_b(el)


