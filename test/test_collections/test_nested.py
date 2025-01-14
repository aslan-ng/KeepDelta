import unittest

from keepdelta.types.collections import Delta
from keepdelta.config import keys


class TestDeltaNested(unittest.TestCase):

    def test_0(self):
        """
        Top level is dict
        """
        old = {
            'dict': {
                'bool': False,
                'int': 1,
                'float': 1.1,
                'complex': 1 + 1j,
                'str': 'hello',
            },
            'list': [
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ],
            'tuple': (
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ),
            'set': {
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            },
        }
        new = {
            'dict': {
                'bool': True,
                'int': 3,
                'float': 3.3,
                'complex': 3 + 3j,
                'str': 'world',
            },
            'list': [
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ],
            'tuple': (
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ),
            'set': {
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            },
        }
        delta = {
            'dict': {
                'bool': True,
                'int': 2,
                'float': 2.1999999999999997,
                'complex': 2 + 2j,
                'str': 'world',
            },
            'list': {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            'tuple': {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            'set': {
                keys['add to set']: {
                    True, # bool
                    3, # int
                    3.3, # float
                    3 + 3j, # complex
                    'world' # str
                },
                keys['remove from set']: {
                    False, # bool
                    1, # int
                    1.1, # float
                    1 + 1j, # complex
                    'hello' # str
                }
            },
        }
        self.assertDictEqual(Delta.create(old, new), delta)
        self.assertDictEqual(Delta.apply(old, delta), new)

    def test_1(self):
        """
        Top level is list
        """
        old = [
            # dict
            {
                'bool': False,
                'int': 1,
                'float': 1.1,
                'complex': 1 + 1j,
                'str': 'hello',
            },
            # list
            [
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ],
            # tuple
            (
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ),
            # set
            {
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            },
        ]
        new = [
            # dict
            {
                'bool': True,
                'int': 3,
                'float': 3.3,
                'complex': 3 + 3j,
                'str': 'world',
            },
            # list
            [
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ],
            # tuple
            (
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ),
            # set
            {
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            },
        ]
        delta = {
            # dict
            0: {
                'bool': True,
                'int': 2,
                'float': 2.1999999999999997,
                'complex': 2 + 2j,
                'str': 'world',
            },
            # list
            1: {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            # tuple
            2: {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            # set
            3: {
                keys['add to set']: {
                    True, # bool
                    3, # int
                    3.3, # float
                    3 + 3j, # complex
                    'world' # str
                },
                keys['remove from set']: {
                    False, # bool
                    1, # int
                    1.1, # float
                    1 + 1j, # complex
                    'hello' # str
                }
            },
        }
        self.assertDictEqual(Delta.create(old, new), delta)
        self.assertListEqual(Delta.apply(old, delta), new)

    def test_2(self):
        """
        Top level is tuple
        """
        old = (
            # dict
            {
                'bool': False,
                'int': 1,
                'float': 1.1,
                'complex': 1 + 1j,
                'str': 'hello',
            },
            # list
            [
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ],
            # tuple
            (
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            ),
            # set
            {
                False, # bool
                1, # int
                1.1, # float
                1 + 1j, # complex
                'hello', # str
            },
        )
        new = (
            # dict
            {
                'bool': True,
                'int': 3,
                'float': 3.3,
                'complex': 3 + 3j,
                'str': 'world',
            },
            # list
            [
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ],
            # tuple
            (
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            ),
            # set
            {
                True, # bool
                3, # int
                3.3, # float
                3 + 3j, # complex
                'world', # str
            },
        )
        delta = {
            # dict
            0: {
                'bool': True,
                'int': 2,
                'float': 2.1999999999999997,
                'complex': 2 + 2j,
                'str': 'world',
            },
            # list
            1: {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            # tuple
            2: {
                0: True, # bool
                1: 2, # int
                2: 2.1999999999999997, # float
                3: (2+2j), # complex
                4: 'world', # str
            },
            # set
            3: {
                keys['add to set']: {
                    True, # bool
                    3, # int
                    3.3, # float
                    3 + 3j, # complex
                    'world' # str
                },
                keys['remove from set']: {
                    False, # bool
                    1, # int
                    1.1, # float
                    1 + 1j, # complex
                    'hello' # str
                }
            },
        }
        self.assertDictEqual(Delta.create(old, new), delta)
        self.assertTupleEqual(Delta.apply(old, delta), new)


if __name__ == '__main__':
    unittest.main()