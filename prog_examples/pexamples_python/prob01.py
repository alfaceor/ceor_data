if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    valid_perm_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n]
    valid_perm_list = [list(elem) for elem in itertools.product(range(x+1), range(y+1), range(z+1)) if sum(elem) != n]
