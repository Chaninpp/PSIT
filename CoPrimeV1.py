''' CoPrimeV1 '''
def main():
    ''' for find Relatively prime
    Ex. input  7    14
               81   21
        output YES  NO
               1    7
    '''
    num = func(int(input()), int(input()), [], [])

    if num == 1:
        print("YES")
    else:
        print("NO")

    print(num)

def func(num_1, num_2, check_1, check_2):
    ''' for
    Ex. input  12       while b:
               18           a, b = b, a % b
        return 6        return a
    '''
    if num_1 != 0 and num_2 != 0: # not = 0
        # loop check divisible
        for i in range(1, max(num_1, num_2)+1):
            if num_1 % i == 0: # find num_1 mod i == 0
                check_1.append(i)
            if num_2 % i == 0: # find num_2 mod i == 0
                check_2.append(i)
        # print(check_1) # [1, 2, 3, 4, 6, 12] divisible 12
        # print(check_2) # [1, 2, 3, 6, 9, 18] divisible 18
        check_max = check_1 if check_1[-1] >= check_2[-1] else check_2 # check last index max
        check_min = check_1 if check_1[-1] < check_2[-1] else check_2 # check last index min
        # check_max = [1, 2, 3, 6, 9, 18] << 18
        # check_min = [1, 2, 3, 4, 6, 12] << 12
        for i in range(-1, -len(check_max)-1, -1): # check GCD index[-1] ; [-2] ; [-3] ; ....
            if check_max[i] in check_min: # 18 in [1, 2, 3, 4, 6, 12] ; 9 in [1, 2, 3, 4, 6, 12]
                result = check_max[i] # 6 in [1, 2, 3, 4, 6, 12] : result = 6
                break #                                   ^

        return result

    else:
        return max(num_1, num_2) # if number = 0

main()
