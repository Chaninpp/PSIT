''' Perfect '''
def main(num):
    ''' for '''
    nub = 0
    for i in range(1, num+1):
        nub += check(i)
    print(nub)

def check(num_c):
    ''' for '''
    nub = 0
    if num_c % 2 != 0:
        return 0
    for i in range(1, int(num_c**0.5)+1):
        if num_c % i == 0:
            nub += i
            if i != 1:
                nub += num_c//i
    if nub == num_c:
        return num_c
    return 0
#check(int(input()))

main(int(input()))
