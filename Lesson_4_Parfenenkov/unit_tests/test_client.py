"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from common_msg.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_answer

import time

''' Класс с тестами '''
class TestClient(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {
        RESPONSE: 200
    }

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = time.ctime()
        self.assertEqual(test, {ACTION: PRESENCE, TIME: time.ctime(), USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_answer(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_answer(self.ok_dict), '200 : OK')

    def test_400_answer(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_answer(self.err_dict), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
