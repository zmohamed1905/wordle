from unittest.mock import patch, call

from main import create_letter_dict, check_guess
import unittest


GREEN = '\x1b[32m'
ORANGE = '\x1b[33m'
RED = '\x1b[31m'


class TestWordle(unittest.TestCase):
    drain_dict = {
        'D': 1,
        'R': 1,
        'A': 1,
        'I': 1,
        'N': 1
    }

    rrise_dict = {
        'S': 1,
        'R': 2,
        'I': 1,
        'E': 1
    }

    def test_create_letter_dict_drain(self):
        # 2. ACT
        actual = create_letter_dict('DRAIN')

        # 3. ASSERT
        self.assertDictEqual(self.drain_dict, actual)

    def test_create_letter_dict_zakariya(self):
        actual = create_letter_dict('ZAKARIYA')

        expected = {
            'Z': 1,
            'R': 1,
            'K': 1,
            'A': 3,
            'I': 1,
            'Y': 1
        }
        self.assertDictEqual(expected, actual)

    @patch('builtins.print')
    def test_foo(self, mocked_print):
        check_guess(secret_word='DRAIN', user_guess='RAISE', secret_word_count=self.drain_dict)  # Call unchanged function.

        assert call(f'{ORANGE}R', end=' ') in mocked_print.mock_calls
        assert call(f'{ORANGE}A', end=' ') in mocked_print.mock_calls
        assert call(f'{ORANGE}I', end=' ') in mocked_print.mock_calls
        assert call(f'{RED}S', end=' ') in mocked_print.mock_calls
        assert call(f'{RED}E', end=' ') in mocked_print.mock_calls

