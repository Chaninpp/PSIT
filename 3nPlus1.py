''' 3nPlus1 '''
def main():
    ''' for '''
    nub = 1
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            while num != 1:
                if num % 2 == 0:
                    num /= 2
                    nub += 1
                else:
                    num *= 3
                    num += 1
                    nub += 1
            print(nub)
            nub = 1

main()
