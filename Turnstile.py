''' Turnstile '''
def main():
    ''' count pass '''
    nub = 0
    num = 0
    while True:
        check = input()
        if check == 'END':
            break
        if check == 'C':
            num = 1
        if check == 'P':
            if num == 1:
                num = 0
                nub += 1
    print(nub)

main()
