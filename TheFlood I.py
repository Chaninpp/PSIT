''' TheFlood I '''
def main():
    ''' for '''
    nub = 0
    foods = [int(i) for i in input().split()]
    while 0 not in foods:
        foods.sort()
        for i in range(1, len(foods)):
            foods[i] -= 1
        nub += 1
    print(nub)
main()
