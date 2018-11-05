''' Largest Number '''
def main(num):
    ''' function's docstring '''
    full = [num[0]+num[1]+num[2], num[0]+num[2]+num[1], num[1]+num[0]+num[2], \
    num[1]+num[2]+num[0], num[2]+num[0]+num[1], num[2]+num[1]+num[0]]
    num = 0
    for i in range(6):
        if int(full[i]) >= num:
            num = int(full[i])
    print(num)

main([input(), input(), input()])
