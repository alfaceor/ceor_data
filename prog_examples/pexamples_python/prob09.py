#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'calculate_gc_content' function below.
#
# The function is expected to return a FLOAT.
# The function accepts STRING sequence as parameter.
#

def calculate_gc_content(sequence):
    # Write your code here
    seq_len = len(sequence)
    if seq_len == 0:
        return (0.00)
    else:
        GpC_pattern = re.compile(r'[gGcC]')
        GpC_content = list(re.findall(GpC_pattern, sequence) )
        # print(GpC_content)
        # print([ a.match for a in GpC_content])
        return (float(len(GpC_content))/float(seq_len) )

if __name__ == '__main__':
    # Use sys.stdin.read() for reading input instead of input() or raw_input()
    # Write your code here

    # fasta_pattern = re.compile(r'>(\w+)\n([^>]+)', re.DOTALL)
    fasta_pattern = re.compile(r'>(.+)\n([^>]+)')
    str_input = sys.stdin.read()
    for fasta_match in re.finditer(fasta_pattern, str_input):
        # print(fasta_match)
        str_header   = fasta_match.group(1)
        str_sequence = re.sub(r'\n', '', fasta_match.group(2))
        # str_sequence = fasta_match.group(2)
        # print("str_header: ", str_header)
        # print("str_sequence: ", str_sequence)
        print("{0:.2f}%".format( 100*calculate_gc_content(str_sequence)) )


