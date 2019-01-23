''' Milk '''
def main(cost, cover, bottle, money):
    ''' Milk '''
    num_bottles = money//cost                   # จำขวดทั้งหมด
    num_covers = num_bottles                    # จำนวนฝา
    while num_covers >= cover and cover > 0:
        temp1 = (num_covers//cover)*bottle      # จำนวนขวดที่ได้แถม
        temp2 = num_covers%cover                # จำนวนฝาที่เหลือ
        num_bottles += temp1                    # จำนวนขวดที่ได้เพิ่ม
        num_covers = temp1 + temp2              # จำนวนฝา = ฝาที่เหลือ + ฝาจากขวด
    return num_bottles

print(main(int(input()), int(input()), int(input()), int(input())))
