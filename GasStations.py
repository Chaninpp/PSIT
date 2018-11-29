''' GasStations '''
def main(dis, fill):
    ''' for '''
    amount = [float(input()) for _ in range(int(input()))]
    temp = []
    start = 0
    end = start + fill
    nub = 0
    while True:
        if end >= dis:
            print(nub)
            break
        else:
            for i in amount:
                if start < i <= end:
                    temp.append(i)
            if temp != []:
                nub += 1
                start = temp[-1]
            else:
                print("depleted")
                break
            end = start + fill
            temp = []
main(float(input()), float(input()))
