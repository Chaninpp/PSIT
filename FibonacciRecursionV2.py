''' FibonacciRecursionV2 '''
def main():
    ''' for print '''
    print(fibonanci(int(input()))[0])

def fibonanci(num):
    ''' for calculate '''
    if num == 0:
        return 0, 1
    else:
        num_1, num_2 = fibonanci(num//2)
        num_3 = num_1 * (num_2 * 2 - num_1)
        num_4 = num_1 * num_1 + num_2 * num_2
        if num % 2 == 0:
            return num_3, num_4
        else:
            return num_4, num_3 + num_4

main()
