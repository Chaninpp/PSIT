''' Duplicate I '''
def main(num1, num2):
    ''' for '''
    set_1 = set([int(input()) for _ in range(num1)])
    set_2 = set([int(input()) for _ in range(num2)])
    result = sorted(list(set_1&set_2), reverse=True)
    if result != []:
        print(*result, sep='\n')
    else:
        print('Nope')

main(int(input()), int(input()))
