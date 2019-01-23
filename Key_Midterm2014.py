''' Key_Midterm2014 '''
def main(num):
    ''' print '''
    # 1
    num_sum = sum([int(i) for i in num])
    # 2
    num2 = int(num[10:])*10
    # calculate
    result = num_sum + num2
    result += 1000*(result < 1000)
    # print
    result = str(result)
    return result[-4:]

print(main(input()))
