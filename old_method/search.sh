#!/bin/bash
for i in {0..10}; do 
    echo -e "CURRENT OFFSET: $i\n\n\n"; 
    head --bytes 2000 output_bits | ./unpack.py | ./pack_bits.py $i; 
    read; 
    clear; 
done
