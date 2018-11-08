''' FoodGrade I '''
def main(num=0):
    ''' for call function check '''
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    num += check()
    print(num)

def check():
    """input """
    weight = float(input())
    if (weight >= 50) and (weight <= 70):
        return 1
    else:
        return 0

main()
