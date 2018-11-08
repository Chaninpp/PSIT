''' GCD_N '''
from fractions import gcd
from functools import reduce
def main():
    ''' for '''
    print(reduce(gcd, [int(input()) for _ in range(int(input()))]))

main()
