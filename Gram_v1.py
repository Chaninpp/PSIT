''' Gram_v1 '''
def main(cha, lis_cha):
    ''' for '''
    old = 0
    for i in range(len(cha)-1): # WOWWOWO
        lis_cha.append(cha[i:i+2])
        # lis_cha = ['WO', 'OW','WW', 'WO', 'OW', 'WO' ]
    for i in range(len(lis_cha)):
        if lis_cha.count(lis_cha[i]) > old:
            old = lis_cha.count(lis_cha[i])
            result = [lis_cha[i], lis_cha.count(lis_cha[i])] # ['WO', 3]

    print(*result, sep='\n')
main(input(), [])
