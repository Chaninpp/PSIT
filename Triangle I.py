''' Triangle I '''
def main():
    ''' Pythagorus's Theorem '''
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    tilted = num3 if num3 > num2 and num3 > num1 else num1 if num1 > num2 else num2
    base = num3 if num3 < num2 and num3 < num1 else num1 if num1 < num2 else num2
    hight = num1 + num2 + num3 - (tilted + base)
    print(calcu(base, hight, tilted))

def calcu(numa, numb, numc):
    ''' for calculate '''
    # print(numa, numb, numc)
    result = numa**2 + numb**2
    if result == numc**2 and numa > 0 and numb > 0:
        # print(result - numc**2)
        return 'Yes'
    return 'No'

main()
