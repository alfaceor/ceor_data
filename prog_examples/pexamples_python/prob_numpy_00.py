#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
if __name__ == '__main__':
    aaa = tuple( map(int, input().split()))
    # print(aaa)
    print(np.zeros(aaa, dtype = np.uint8))
    print(np.ones(aaa, dtype = np.uint8))
