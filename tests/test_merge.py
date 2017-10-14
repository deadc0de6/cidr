"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6
unittest for "merge"
"""

import unittest

from cidr import Pycidr


class TestMerge(unittest.TestCase):

    def test_merge(self):
        '''Test merge ranges'''
        pycidr = Pycidr()

        rngs = pycidr.merge(['192.168.0.0/30'])
        rngs = [str(x) for x in rngs]
        self.assertTrue(set(rngs) == set(['192.168.0.0/30']))

        l = ['192.168.0.0/30', '192.168.0.4',
             '192.168.0.5', '192.168.0.6', '192.168.0.7']
        rngs = pycidr.merge(l)
        rngs = [str(x) for x in rngs]
        self.assertTrue(set(rngs) == set(['192.168.0.0/29']))

        rngs = pycidr.merge(['10.0.0.1', 'unknown'])
        print(rngs)
        rngs = [str(x) for x in rngs]
        print(rngs)
        self.assertTrue(set(rngs) == set(['10.0.0.1/32']))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
