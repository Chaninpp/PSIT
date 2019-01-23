''' Refrigerator '''
def main(temp):
    ''' for '''
    nub = 0
    foods = [int(i) for i in input().split()]
    while 0 not in foods:
        foods.sort()
        for i in range(1, temp):
            foods[i] -= 1
        nub += 1
    # print(foods)
    print(nub)
main(int(input()))
