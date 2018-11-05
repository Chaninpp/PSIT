''' GCD_v2 '''
def main(num_1, num_2):
    ''' for
    Ex. input  12
               18
        return 6
    '''
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2
    print(num_1)

main(int(input()), int(input()))
