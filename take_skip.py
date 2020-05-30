#!/usr/bin/python

import sys

take = int(sys.argv[1])
skip = int(sys.argv[2])

offset = int(sys.argv[3])

sys.stdin.read(offset)

chunk_size = take + skip

while 1:
    data = sys.stdin.read(chunk_size)
    if len(data) != chunk_size:
        break

    sys.stdout.write(chr(int(data[0:take][::-1], 2)))
    sys.stdout.flush()
