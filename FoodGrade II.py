''' FoodGrade II '''
def main(weight):
    ''' for '''
    nub, result = 0, 0
    num = sorted([int(i) for i in input().split()])
    for i in num:
        if i+nub <= weight:
            nub += i
            result += 1
        else:
            break
    print(result)

main(int(input()))
