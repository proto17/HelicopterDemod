#!/usr/bin/python

import sys

chunk_size = 100

while 1:
    data = sys.stdin.read(chunk_size)
    if len(data) != chunk_size:
        break

    sys.stdout.write(''.join(['1' if x == '\x00' else '0' for x in data]))
    sys.stdout.flush()

