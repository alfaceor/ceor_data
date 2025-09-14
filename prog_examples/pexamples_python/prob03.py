#!/usr/bin/env python
if __name__ == '__main__':
    records_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records_list.append([name, score])
    # print(records_list)

    # records_list_sorted = sorted(records_list, key=lambda x: x[1], reverse=True)
    records_list_sorted = sorted(records_list, key=lambda x: x[1], reverse=True)

    # print(records_list_sorted)
    elem_1st_lowest = records_list_sorted.pop()
    val_1st_lowest = elem_1st_lowest[1]
    val_2nd_lowest = None
    list_2nd_lowest = list()
    
    b_2nd_lowest = True
    while (b_2nd_lowest and ( len(records_list_sorted) > 0 ) ): # Need to add if list is None meaning all are the same value, there is no 2nd lowest 
        elem = records_list_sorted.pop()
        if elem[1] != val_1st_lowest:
            if val_2nd_lowest is None: # 2nd lowest value found
                val_2nd_lowest = elem[1]
                list_2nd_lowest.append(elem[0])
            else:
                if elem[1] == val_2nd_lowest:
                    list_2nd_lowest.append(elem[0])
                else:
                    b_2nd_lowest = False

    print("\n".join( sorted(list_2nd_lowest)))


    
