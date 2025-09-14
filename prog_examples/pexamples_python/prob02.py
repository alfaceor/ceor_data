if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    pos1_val = arr.max()
    pos2_val = arr.remove(pos1_val).max()
    print(pos2_val)
