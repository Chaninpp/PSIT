''' Run Length Encoding '''
def main(cha, lis, result):
    '''
    Ex. aaabbbbaaaa = 3a4b4a
    '''
    cha_old = cha[0] # first check

    for i in range(len(cha)):
        if cha_old == cha[i]: # check cha if cha_old = 'a' == cha[2] = 'a'
            lis += cha[i]     # lis = aa
            cha_old = cha[i]  # cha_old = 'a'
        else:                 # if cha_old = 'a' != cha[3] = 'b'
            lis += ' '        # lis = 'aaa '
            lis += cha[i]     # lis = 'aaa b'
            cha_old = cha[i]  # cha_old = cha[3] = 'b'
    # lis = aaa bbbb aaaa
    lis = lis.split() # ['aaa', 'bbbb', 'aaaa']

    for i in range(len(lis)): # count cha in index lis[i]
        result += str(lis[i].count(lis[i][0]))+lis[i][0] # 'aaa'.count(a)+'a'
    print(result)

main(input(), '', '')
