"""
How to run tests:
    $ cd test_project
    $ PYTHONPATH=../ ./manage.py test loginza
"""

from django.test import TestCase
from loginza.utils import get_next_username


class TestUtilsGetNextUsername(TestCase):
    def test_should_return_random_value(self):
        for i in range(10):
            self.assertNotEqual(get_next_username(), get_next_username())

    def test_should_return_ascii_value(self):
        response = get_next_username()
        try:
            response.decode('ascii')
            is_raised = False
        except UnicodeDecodeError:
            is_raised = True

        self.assertFalse(is_raised, 'get_next_username should return ascii encoded value')

    def test_should_return_value_without_spaces(self):
        response = get_next_username()
        self.assertFalse(' ' in response)

    def test_should_return_30_chars_length_value(self):
        response = get_next_username()
        msg = 'should return 30 chars length value, because User.username field max_length=30'
        self.assertEqual(len(response), 30, msg=msg)