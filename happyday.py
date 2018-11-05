''' happyday '''
def main():
    ''' for check
    if number >= 80                                      +1
    if number >= 20 and number[i] - number[i-1] >= 10    +1
    '''
    num = input().split(',')
    count = 0
    for i in range(len(num)):
        if int(num[i]) >= 80:
            count += 1
        elif i > 0:
            if int(num[i])-int(num[i-1]) >= 10 and int(num[i]) >= 20:
                count += 1

    print(count)

main()
