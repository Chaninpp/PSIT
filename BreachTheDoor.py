''' BreachTheDoor '''
def main(cha, cha_all, result):
    ''' for nub '''
    # input = Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    for i in range(len(cha)):
        if cha[i].isalpha() or cha[i] == ' ': # cut special alphabet
            cha_all += cha[i]
    # cha = Lorem ipsum dolor sit amet consectetur adipiscing elit
    cha_all = cha_all.split()
    # cha_all = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
    for i in range(len(cha_all)): # check word > 6
        if len(cha_all[i]) > 6:
            result += cha_all[i]+' '
    print(result)

main(input(), '', '')
