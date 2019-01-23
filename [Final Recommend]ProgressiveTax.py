''' [Final Recommend]ProgressiveTax '''
def main(money):
    ''' for '''
    nub = 0
    lis_if = [4000000, 2000000, 1000000, 750000, 500000, 300000, 150000]
    lis_percent = [35, 30, 25, 20, 15, 10, 5]
    for i in range(7):
        if money >= lis_if[i]:
            temp = money-lis_if[i]
            nub += (temp*lis_percent[i])//100
            money -= temp

    print(nub)

main(int(input()))
