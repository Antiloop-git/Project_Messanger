"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""


import subprocess
import chardet


ARGS1 = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'youtube.com']
lst = [ARGS1, ARGS2]

def test_ping(arg):
    site_ping = subprocess.Popen(arg, stdout=subprocess.PIPE)
    for line in site_ping.stdout:
        result = chardet.detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

for el in lst:
    test_ping(el)
