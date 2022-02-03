"""Декораторы"""

import sys
import logging
import logs.config_server_log
import logs.config_client_log
import traceback
import inspect
from common_msg.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT


# метод определения модуля, источника запуска.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.
# os.path.split(sys.argv[0])[1]
if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    LOGGER = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    LOGGER = logging.getLogger('client')


# Реализация в виде функции
# def log(func_to_log):
#     """Функция-декоратор"""
#     def log_saver(*args, **kwargs):
#         """Обертка"""
#         ret = func_to_log(*args, **kwargs)
#         LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
#                      f'Вызов из модуля {func_to_log.__module__}. Вызов из'
#                      f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
#                      f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2)
#         return ret
#     return log_saver


# Реализация в виде класса
class Log:
    """Класс-декоратор"""
    def __call__(self, func_to_log):
        def log_saver(*args, **kwargs):
            """Обертка"""
            ret = func_to_log(*args, **kwargs)
            LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                         f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                         f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                         f'Вызов из функции {inspect.stack()[1][3]}', stacklevel=2)

            if func_to_log.__name__ == 'create_presence':
                LOGGER.debug(f'Сформировано {PRESENCE} сообщение от пользователя {args}', stacklevel=2)

            if func_to_log.__name__ == 'process_answer':
                LOGGER.debug(f'Разбор сообщения от сервера: {args}', stacklevel=2)

            if func_to_log.__name__ == 'process_client_message':
                LOGGER.debug(f'Разбор сообщения от клиента {args}', stacklevel=2)

            return ret
        return log_saver
