''' GasStations '''
def main(dis, fill):
    ''' for '''
    amount = [float(input()) for _ in range(int(input()))]
    temp = []
    start = 0
    end = start + fill
    nub = 0
    while True:
        if end >= dis: # จบ
            print(nub)
            break
        else:
            for i in amount: # หา ปตท.
                if start < i <= end:
                    temp.append(i)
            if temp != []:
                nub += 1
                start = temp[-1] # ปตท. ไกลสุด
            else:
                print("depleted") # ไม่เจอ ปตท.
                break
            end = start + fill # ระยะทางต้องเติม
            temp = [] 
main(float(input()), float(input()))
