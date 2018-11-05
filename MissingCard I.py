''' MissingCard I '''
def main(nub, check):
    ''' for '''
    for i in range(2, 11):
        check.update({str(i)+'S', str(i)+'H', str(i)+'D', str(i)+'C'})
    for i in 'AKQJ':
        check.update({str(i)+'S', str(i)+'H', str(i)+'D', str(i)+'C'})
    for _ in range(51):
        nub.add(input())
    print(*(check-nub))

main(set(), set())
