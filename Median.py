''' Median '''
def main():
    ''' for
    Ex. 5       819.0
        424
        562
        819
        866
        965
    '''
    num = sorted([int(input()) for _ in range(int(input()))])
    if len(num) % 2 != 0:
        print('%.1f'%num[len(num)//2])
    else:
        print('%.1f'%((num[(len(num)//2)-1]+num[(len(num)//2)])/2))

main()
