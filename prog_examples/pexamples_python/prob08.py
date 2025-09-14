def wrapper(f):
    def fun(l):
        # complete the function
        new_l = list()
        for input_number in l:
            if len(input_number) == 10:
                input_number = "+91 " + input_number[0:5] + " "  + input_number[5:10]
                new_l.append(input_number)
            else:
                if input_number[0] == '0':
                    input_number = "+91 " + input_number[1:6] + " " + input_number[6:]
                    new_l.append(input_number)
                elif input_number[0:3] == "+91":
                    input_number = input_number[0:3] + " " + input_number[3:8] + " " + input_number[8:]
                    new_l.append(input_number)
                elif input_number[0:2] == "91":
                    input_number = "+" + input_number[0:2] + " " + input_number[2:7] + " " + input_number[7:]
                    new_l.append(input_number)
                else:
                    input_number = input_number[0:3] + " " + input_number[3:8] + " " + input_number[8:]
                    new_l.append(input_number)
                    
                
        return f(new_l)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
