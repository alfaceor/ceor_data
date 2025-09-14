if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        output = 0
        expo = 1
        factor = 10
        for i in range(1, n + 1):
            if (i == 10**expo):
                breakpoint()
                factor = factor*10
                expo = expo + 1
            output = output * factor + i
        print(output)

