''' FibonacciRecursionV1 '''
def main():
    ''' for '''
    num = int(input())
    result = ((1+(5**0.5))**num-(1-(5**0.5))**num)/(2**num*(5**0.5))
    print('%d'%result)

main()
