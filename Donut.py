''' Donut '''
def main():
    ''' find buy donut '''
    price = float(input())
    buy = float(input())
    free = float(input())
    want = float(input())
    donuts = 0
    price_buy = 0

    buy_free = buy + free
    want_free = want // buy_free
    left = want % buy_free

    if left >= buy:
        want_free += 1
    else:
        donuts += left
        price_buy += (left * price)

    donuts += (buy_free * want_free)
    price_buy += (want_free * buy * price)

    print("%.2f Baht\n%d"%(price_buy, donuts))

main()

