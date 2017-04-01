#!/usr/bin/env python3

"""
author: deadc0de6 (https://github.com/deadc0de6)
Copyright (c) 2017, deadc0de6

IPv4 addresses and CIDR tool

ref:
    https://docs.python.org/3/library/ipaddress.html
    http://netaddr.readthedocs.io/en/latest/

"""

import sys
import os
import netaddr
import ipaddress
from docopt import docopt

VERSION = '0.1'
VERBOSE = False

USAGE = """

cidr.py

Usage:
    cidr.py count [--verbose] [--] <path-or-cidr>...
    cidr.py explode [--verbose] [--] <path-or-cidr>...
    cidr.py merge [--verbose] [--] <path-or-cidr>...
    cidr.py intersect [--verbose] --left=<path> --right=<path>
    cidr.py (-h | --help)
    cidr.py (-v | --version)

Options:
    --left=<path>       Path containing one IP/CIDR per line.
    --right=<path>      Path containing one IP/CIDR per line.
    --verbose           Be verbose [default: False].
    -v --version        Show version.
    -h --help           Show this screen.

"""


class Pycidr:

    def __init__(self):
        self.parser = Parser()

    def _err(self, string):
        """ output to stderr """
        sys.stderr.write('%s\n' % (string))

    def _parse(self, arg):
        return self.parser.parse(arg)

    def _load_entire_file(self, path):
        """ load entire file content in memory """
        with open(path, 'r') as f:
            return [str(x) for x in parse_file(f)]

    def count(self, args):
        """ count total number of IPs """
        tot = 0
        for arg in args:
            for ip in self._parse(arg):
                if type(ip) == netaddr.IPAddress:
                    cnt = 1
                else:
                    cnt = len(ip)
                if VERBOSE:
                    self._err('[DBG] %s -> %u' % (ip, cnt))
                tot += cnt
        return tot

    def explode(self, args):
        """ explode all ranges """
        for arg in args:
            for ips in self._parse(arg):
                if type(ips) == netaddr.IPAddress:
                    yield ips
                else:
                    for ip in ips:
                        yield ip

    def merge(self, args):
        """ merge all possible addresses """
        l = []
        for arg in args:
            for ips in self._parse(arg):
                l.append(ips)
                l = netaddr.cidr_merge(l)
        return netaddr.cidr_merge(l)

    def intersect(self, left, right):
        """ check if left is contained in right """
        results = {}
        sources = [ipaddress.IPv4Network(x, strict=False)
                   for x in self.parser.parse(left)]
        for ips in self.parser.parse(right):
            dst = ipaddress.IPv4Network(ips, strict=False)
            for src in sources:
                if src.overlaps(dst):
                    if VERBOSE:
                        self._err('[DBG] %s overlaps with %s' % (str(src),
                                                                 str(dst)))
                    results.setdefault(src, []).append(str(dst))
        for src in sources:
            if src in results.keys():
                v = results[src]
                src = str(src)
                pot = netaddr.cidr_merge(v)[0]
                if netaddr.IPNetwork(src) in pot:
                    print('%s is entirely contained in %s' % (src, str(pot)))
                else:
                    print('%s is partially contained in %s' % (src, str(pot)))
            else:
                print('%s was not found' % (src))


class Parser:

    def __init__(self):
        pass

    def parse(self, arg):
        if os.path.exists(arg) and os.path.isfile(arg):
            return self._parse_file(arg)
        return self._parse_line(arg)

    def _parse_line(self, line):
        """ parse a single line containing an address """
        try:
            if '-' in line:
                ip = netaddr.IPRange(line.split('-')[0], line.split('-')[1])
                return netaddr.cidr_merge(ip)
            elif '/' in line:
                ip = netaddr.IPNetwork(line)
            else:
                ip = netaddr.IPAddress(line)
            return [ip]
        except:
            print('parsing failed for ', line)
            return []

    def _parse_file(self, path):
        """ parse a file"""
        with open(path, 'r') as f:
            for line in f:
                line = line.rstrip()
                if line.startswith('#'):
                    continue
                if line == '':
                    continue
                tmp = self._parse_line(line)
                if not tmp:
                    continue
                if type(tmp) == list:
                    for i in tmp:
                        yield i
                else:
                    yield tmp

if __name__ == '__main__':
    """ entry point """
    args = docopt(USAGE, version=VERSION)
    VERBOSE = args['--verbose']

    pycidr = Pycidr()

    if args['count']:
        tot = pycidr.count(args['<path-or-cidr>'])
        print('Total number of IPs: %u' % (tot))
    elif args['explode']:
        ips = pycidr.explode(args['<path-or-cidr>'])
        for ip in ips:
            print(ip)
    elif args['merge']:
        rngs = pycidr.merge(args['<path-or-cidr>'])
        for rng in rngs:
            print(rng)
    elif args['intersect']:
        left = args['--left']
        right = args['--right']
        pycidr.intersect(left, right)

    sys.exit(0)
