''' AlmostMean '''
def main(nub, ave, lis):
    ''' for '''
    num = [input().split() for _ in range(nub)]
    ave = sum([float(num[i][1]) for i in range(nub)]) / nub
    value = ave
    for i in range(nub):
        check = float(num[i][1])
        if ave > check and value > ave - check:
            lis = num[i]
            value = ave - check
    print(lis[0]+'\t'+lis[1])

main(int(input()), 0, '')
