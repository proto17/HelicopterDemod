#!/usr/bin/python

import sys

patt_one = '11000000'
patt_two = '01000000'

# Each 'word' is 10 bits, and we are looking for two words
needed_bits = 10 * 2

# Initialize the buffer
bit_buff = sys.stdin.read(needed_bits)

# Make sure that enough data was read to fill the buffer
if len(bit_buff) != needed_bits:
    sys.exit(1)

# Loop until the pattern is found
while 1:
    # We want the buffer to be '11000000XX01000000XX' so that the take-skip operation can
    # immediately pick up with take 8, skip 2
    if bit_buff[:8] == patt_one and bit_buff[-10:-2] == patt_two:
        # Pattern found, exit out of the loop
        break
    
    # Haven't found the pattern yet, so shift in a new bit (ASCII '1' or '0')

    # First thing is to remove the first bit from the buffer (left-most)
    bit_buff = bit_buff[1:]
    # Then read in a new bit and verify that the bit was actually read (might be at end of stream)
    new_bit = sys.stdin.read(1)

    # Exit out if reached end of stream
    if len(new_bit) == 0:
        break

    # Append the new bit to the end (right side) of the buffer
    bit_buff += new_bit[0]

# At this point we are sync'd up on the correct start bit, so just output all remaining bits

# Reading in data one chunk at a time as single byte reads are *really* slow
chunk_size = 100

while 1:
    # Read the data in, write the data out
    data = sys.stdin.read(chunk_size)
    sys.stdout.write(data)

    # If the number of bytes read doesn't match the expected value, that likely means the end of stream has been reached
    if len(data) != chunk_size:
        break
