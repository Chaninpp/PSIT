''' Kaprekar's Constant '''
def main(number):
    ''' function's docstring '''
    nub = 0
    while True:
        if number == "6174":
            break
        else:
            boat = main2(str(number))
            number = "%04d"%(int(boat[0]) - int(boat[1]))
            nub += 1
    print(nub)

def main2(first):
    ''' function s0rt all number '''
    num = list(first)
    while True:
        nub = 0
        for i in range(len(num)-1): # check all number
            if int(num[i]) <= int(num[i+1]):
                nub += 1
            else:
                break
        if nub == len(num)-1: # all number pass
            break
        else:
            for i in range(len(num)-1):
                num_check = s0rt(int(num[i]), int(num[i+1]))
                num[i], num[i+1] = num_check[0], num_check[1]
    return ''.join(num[::-1]), ''.join(num)

def s0rt(num1, num2):
    ''' function s0rting '''
    if num1 > num2:
        num1, num2 = num2, num1
        return str(num1), str(num2)
    else:
        return str(num1), str(num2)

main(input()) # <<< Start
