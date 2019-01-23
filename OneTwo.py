''' OneTwo '''
def main(num):
    ''' for '''
    lis = ['1', '2']
    for _ in range(2, num):
        new = lis[1]+lis[0]
        lis[0] = lis[1]
        lis[1] = new
    return lis[1] if num != 1 else lis[0]
print(main(int(input())))
