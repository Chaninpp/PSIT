''' Binary '''
def main(num):
    ''' for Decimal transform Binary '''
    binary = '' if num > 0 else '0'
    while True:
        if num < 1:
            break
        binary += str(num%2)
        num //= 2
    print(*binary[-1::-1], sep='')

main(int(input()))
