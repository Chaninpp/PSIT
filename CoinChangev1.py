''' CoinChangev1 '''
def main(coin):
    ''' for calculate '''
    c_25 = coin//25
    c_10 = (coin%25)//10
    c_5 = ((coin%25)%10)//5
    c_1 = (((coin%25)%10)%5)//1
    print(c_25+c_10+c_5+c_1)

main(int(input()))
