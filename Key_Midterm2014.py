''' Key_Midterm2014 '''
def main():
    ''' print '''
    num = input()
    num1 = 0
    # 1
    for i in range(13):
        num1 += int(num[i])
    # 2
    num2 = int(num[10:])*10
    # calculate
    result = num1 + num2
    result += 1000*(result < 1000)
    # print
    result = str(result)
    print(result[-4:])

main()
