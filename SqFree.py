''' SqFree '''
def main(num, check):
    ''' for square-free number '''
    for i in range(1, num+1):
        check += squarefree(i)
    print(check)

def squarefree(num_c):
    ''' for '''
    check = round(num_c**0.5)
    if num_c < 2:
        return 1
    if check * check == num_c:
        return 0
    if check <= 2:
        return 1
    for i in range(2, check):
        if num_c % i**2 == 0 and i**2 <= num_c:
            return 0
    return 1

main(int(input()), 0)
