''' Indicator_Right '''
def main():
    ''' for print * x k '''
    numk = int(input())
    numn = int(input())
    for i in range(numn//2+1):
        print((' '*i)+'*'*numk)
    for i in range(numn//2-1, -1, -1):
        print((' '*i)+'*'*numk)
main()
