"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6
unittest for "count"
"""

import unittest

from cidr import Pycidr


class TestCount(unittest.TestCase):

    def test_count(self):
        '''Test count number of IPs'''
        TESTS = {
                256: ['192.168.0.0/24'],
                1: ['10.0.0.1'],
                512: ['192.168.0.0/24', '10.0.0.0/24'],
                4: ['10.0.0.0/30', 'something'],
                0: ['invalid'],
                4: ['else', '10.0.0.0/30'],
                255: ['127.0.1.0-127.0.1.250', '10.0.1.0/30'],
                2**32: ['0.0.0.0/0']
            }
        pycidr = Pycidr()
        for k, v in TESTS.items():
            cnt = pycidr.count(v)
            print(k)
            print(v)
            print('---> ', cnt)
            self.assertTrue(cnt == k)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
