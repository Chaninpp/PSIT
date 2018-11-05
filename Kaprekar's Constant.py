''' Kaprekar's Constant '''
def main(number):
    ''' function's docstring '''
    nub = 0
    while True:
        if number == 6174:
            break
        else:
            boat = main2(str(number))
            num1 = boat[0]
            num2 = boat[1]
            number = int(num1) - int(num2)
            nub += 1
            number *= 1000 if number < 10 else 100 if number < 100 else 10 if number < 1000 else 1
    print(nub)

def main2(first):
    ''' for all s0rt '''
    num = []
    for i in first:
        num.append(i)
    while True:
        nub = 0
        for i in range(len(num)-1):
            if int(num[i]) <= int(num[i+1]):
                nub += 1
            else:
                break
        if nub == len(num)-1:
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

# Reserve
def main3(num):
    ''' for game 6174 '''
    first, sec, thir, four, = 0, 0, 0, 0
    for i in num:
        if int(i) >= int(first):
            four = thir
            thir = sec
            sec = first
            first = i
        elif int(first) > int(i) >= int(sec):
            four = thir
            thir = sec
            sec = i
        elif int(sec) > int(i) >= int(thir):
            four = thir
            thir = i
        elif int(thir) > int(i) >= int(four):
            four = i
    num_ma = first+sec+thir+four
    num_mi = num_ma[::-1]
    # print(num_ma, num_mi, '=', int(num_ma)-int(num_mi))
    return num_ma, num_mi

