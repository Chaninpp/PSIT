''' compoundinterest '''
def main():
    ''' for calculate inflation'''
    num = float(input())
    num_1 = 1+float(input())/100
    for _ in range(int(input())):
        num *= num_1
    print('%.2f'%num)

main()
