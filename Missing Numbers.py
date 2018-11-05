''' Missing Numbers '''
def main(num, check, num_1):
    ''' for
    Ex. input  = 10 : 9 : 4 : 6 : 1 : 7 : 5 : 2 : 10 : 0
        output = 3 : 8
    '''
    for i in range(num+1):
        check.append(i) # run check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    while num_1 != 0:
        num_1 = int(input())
        check.remove(num_1) # check.remove(9) ; check.remove(4) ; ...

    print(*check, sep='\n')

main(int(input()), [], '')
