#!/usr/bin/python

import sys

sys.stdin.read(int(sys.argv[1]))

while 1:
    a = sys.stdin.read(10)

    if len(a) != 10:
        break
    a = a[:8]

    sys.stdout.write(chr(int(a[::-1], 2)))

sys.stdout.flush()
