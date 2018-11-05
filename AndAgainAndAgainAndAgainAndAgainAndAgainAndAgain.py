''' AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain '''
def main(result, cha):
    ''' Ex. input amet ut ve et a netus arcu fames.
            ouput ['amet', 'arcu', 'fames', 'netus']
    '''
    cha = cha.split(' ') # ['amet', 'ut', 've', 'et', 'a', 'netus', 'arcu', 'fames.']
    # print(cha)

    for i in range(len(cha)):
        nub = 0 # count 'aeiou'
        for j in range(len(cha[i])):
            if cha[i][j] in 'aeiou': # nub += 1 if cha in 'aeiou'
                nub += 1
        if nub >= 2: # if word 'aeiou' >= 2 correct
            result.append(cha[i].strip(".")) # but fames.
                                             # del .    ^
    # ['amet', 'netus', 'arcu', 'fames']
    result.sort()
    # ['amet', 'arcu', 'fames', 'netus']

    if len(result) > 0:
        print(*result, sep='\n')
    else:
        print('Nope')

main([], input())
