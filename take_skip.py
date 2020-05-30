#!/usr/bin/python

# No fancy getopt here.  Good old fashion argv calls that blow up in your face with 
# meaningless error messages.  May God have mercy on your souls.  Because I didn't.

# The 'take' happens before the 'skip'!!

import sys

# Number of bits to keep
take = int(sys.argv[1])
# Number of bits to skip
skip = int(sys.argv[2])

# Number of bytes to skip from the input before starting the actual 'take-skip'
offset = int(sys.argv[3])

# Throw away the first `offset` bytes
sys.stdin.read(offset)

# The number of bytes to read in with each call to stdin.read needs to be the 
# number of skip bytes plus the number of take bytes.  This maintains alignment.
# Could also be some multiple if you want to speed up the IO operations.
chunk_size = take + skip

# Loop until there's no data on stdin
while 1:
    # Read in one chunk of data
    data = sys.stdin.read(chunk_size)
    
    # Not getting back a full chunk means that the input stream is empty, so exit out
    if len(data) != chunk_size:
        break
    
    # Extract out the first `take` bytes, reverse them, then convert the bits to an int, then to a char
    sys.stdout.write(chr(int(data[0:take][::-1], 2)))
    sys.stdout.flush()
