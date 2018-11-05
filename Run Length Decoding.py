''' Run Length Decoding '''
def main(cha, nub, lis):
    '''
    Ex. 10a5d6c17f = aaaaaaaaaadddddccccccfffffffffffffffff
    '''
    for i in range(len(cha)):
        if cha[i].isdigit():
            nub += cha[i] # str nub = 1 ; nub = 10
        else:
            lis.append(cha[i]*int(nub)) # lis.append('a' * 10)
            nub = ''
    # lis = ['aaaaaaaaaa', 'ddddd', 'cccccc', 'fffffffffffffffff']
    print(*lis, sep='')

main(input(), '', [])
