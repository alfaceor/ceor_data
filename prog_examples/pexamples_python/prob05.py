#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == "__main__":
    list_X2 = list()
    K, M = map(int, input().split())
    for _ in range(K):
        list_line = input().split()
        list_line.pop(0)
        set_X2_k = set( map(lambda x: ( int(x)**2 ) % M, list_line ) ) # Make a unique of set to avoid redundancy
        list_X2.append(set_X2_k)
    # print(list_X2)
    set_S = set()
    for ii in range(K-1):
        list_X2[ii+1] = { (a+b) % M for a in list_X2[ii] for b in list_X2[ii+1] }
    print(max(list_X2[K-1]))

    # a = {1, 2, 3}
    # b = {10, -10}
    # c = {i+j for i in a for j in b}
    # print (c)

    # for ii, elem in enumerate(itertools.product(*list_X2) ):
    #     sum_elem = sum(elem)
    #     if sum_elem == M - 1:
    #         S_max = sum_elem
    #         break
    #     else:
    #         set_S.add(sum_elem % M)

    
    # S_max = 0 # python mod return positive numbers.

    # for ii, elem in enumerate(itertools.product(*list_X2) ):
    #     sum_elem = sum(elem)
    #     if ii == 0 and sum_elem < M:
    #         S_max = sum_elem
    #         # print(elem, sum_elem, M, mod_sum_elem, S_max)
    #         # print("Max found: ")
    #         # return max_val
    #         break
    #     else:
    #         mod_sum_elem = sum_elem % M
    #         if mod_sum_elem > S_max:
    #             S_max = mod_sum_elem
    #         #print(elem, sum_elem, M, mod_sum_elem, S_max)
    # print(S_max)

        # aaa = list( map(lambda idx: list_X2[*idx], zip(range(K), elem) ) )
        # print(aaa)
    

    
