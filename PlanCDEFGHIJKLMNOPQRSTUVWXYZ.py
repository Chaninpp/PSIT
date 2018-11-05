''' PlanCDEFGHIJKLMNOPQRSTUVWXYZ '''
def main():
    ''' for sort '''
    option = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    much = num3 if num3 > num2 and num3 > num1 else num1 if num1 > num2 else num2
    less = num3 if num3 < num2 and num3 < num1 else num1 if num1 < num2 else num2
    mid = (num1 + num2 + num3) - (much + less)
    if option == 'Ascend':
        print('%.2f, %.2f, %.2f'%(less, mid, much)) # Ascend
    else:
        print('%.2f, %.2f, %.2f'%(much, mid, less)) # Descend

main()
