#!/bin/bash
cat output_bits | ./unpack.py | ./pack_bits.py $1
