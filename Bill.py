''' Bill '''
def main():
    ''' for calculate '''
    num = int(input())
    if num * 0.1 < 50:
        num += 50
    elif num * 0.1 >= 1000:
        num += 1000
    else:
        num *= 1.1
    print('%.2f'%(num*1.07))

main()
