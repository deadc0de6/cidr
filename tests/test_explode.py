"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6
unittest for "explode"
"""

import unittest

from cidr import Pycidr


class TestExplode(unittest.TestCase):

    def test_explode(self):
        '''Test explode range'''
        pycidr = Pycidr()

        rngs = pycidr.explode(['192.168.0.0/30'])
        rngs = [str(x) for x in rngs]
        self.assertTrue(set(rngs) == set(['192.168.0.0',
                                          '192.168.0.1',
                                          '192.168.0.2',
                                          '192.168.0.3']))

        rngs = list(pycidr.explode(['random']))
        self.assertTrue(rngs == [])

        rngs = pycidr.explode(['127.0.0.1'])
        rngs = [str(x) for x in rngs]
        self.assertTrue(set(rngs) == set(['127.0.0.1']))

        rngs = list(pycidr.explode(['10.1.1.0/16']))
        self.assertTrue(len(rngs) == 65536)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
