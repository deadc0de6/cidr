**cidr.py**

[![Build Status](https://travis-ci.org/deadc0de6/cidr.svg?branch=master)](https://travis-ci.org/deadc0de6/cidr)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

Tool helper for managing CIDR.

---

```
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
    -h --help           Show this screen
```

# Count

Count the total number of IPS:

```
$ ./cidr.py count --verbose 192.168.0.0/24 10.0.2.0/24 127.0.0.1
[DBG] 192.168.0.0/24 -> 256
[DBG] 10.0.2.0/24 -> 256
[DBG] 127.0.0.1 -> 1
Total number of IPs: 513
```

# Explode

Explode CIDR range(s)

```
$ ./cidr.py explode 192.168.0.0/30
192.168.0.0
192.168.0.1
192.168.0.2
192.168.0.3
```

# Merge

Merge CIDR ranges

```
$ ./cidr.py merge 192.168.10.10/16 192.168.0.0/24 127.0.1.0/30
127.0.1.0/30
192.168.0.0/16
```

# Intersect

Check how CIDR intersect

```
$ cat ranges4
192.168.0.0/16
10.0.2.0/30
10.0.1.0/30
$ cat ranges1
192.168.0.0/24
10.0.2.0/24
127.0.0.1
$ ./cidr.py intersect --left ranges4 --right ranges1
192.168.0.0/16 is partially contained in 192.168.0.0/24
10.0.2.0/30 is entirely contained in 10.0.2.0/24
10.0.1.0/30 was not found
```

# Contribution

If you want to contribute, feel free to do a PR.

# License

This project is licensed under the terms of the GPLv3 license.

