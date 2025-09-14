#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
if __name__ == '__main__':
    str_S = input()
    print(str_S)
    aaa = itertools.groupby(str_S)
    print(aaa)
    # for i, j in aaa:
    #     print(i)
    #     print(len(list(j))

    lista = [ str( ( len(list(j)), int(i) ) ) for i, j in aaa]
    print(" ".join(lista))
