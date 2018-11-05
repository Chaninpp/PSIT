''' All_Primes '''
def func(num):
    ''' for prime '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    """ input number """
    nub = 0
    num1 = 1
    num2 = int(input())
    for i in range(num1, num2+1):
        if func(i):
            nub += 1
    print(nub)

main()
