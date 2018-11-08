''' WordSequence II '''
def main(cha_1, cha_2):
    ''' for '''
    for j in range(max(len(cha_2), len(cha_1))+1):
        print(cha_2[:j]+cha_1[j:])

main(input(), input())
