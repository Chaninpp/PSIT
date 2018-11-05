''' VerticalHistogram '''
def main(cha):
    ''' for Histogram
    Ex. InformationOfTechnology

    004                     *
    003                   * *
    002       *           * *
    001 * * * * * * * * * * * * * * * * *
        a c e f g h i l m n o r t y I O T
    '''
    dic, cha2, num = {}, [], 0

    for i in cha:
        dic[i] = cha.count(i)
    sett = set(dic)
    lis = sorted(list(sett))
    # dic = cha count
    # lis = cha
    for i in lis: # [A, a]
        if i.isupper() or i == ' ':
            cha2.append(i)
    lis = lis[len(cha2)::]
    lis.extend(cha2) # [a, A]

    num = int(max(dic.items(), key=lambda x: x[1])[1])
    # max(num)
    for i in range(num, 0, -1):
        print('%03d'%(i), end=' ') # 001
        for j in lis:
            if dic[j] >= i:
                print('*', end=' ') # *
            elif dic[j] < i:
                print(' ', end=' ') # ' '
        print()
    print('    ', end='')
    print(*lis) # a b c d

main(input())
