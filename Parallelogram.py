''' Parallelogram '''
def main(cha):
    ''' for '''
    for i in range(len(cha)):
        print(' '*(len(cha)-i-1)+cha[:i+1])
    for i in range(len(cha)):
        print(cha[i+1:])
main(input())
