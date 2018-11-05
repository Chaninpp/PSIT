''' HorizontalHistogram '''
def main():
    ''' for '''
    cha = list(input())
    dic = {}
    cha2 = []

    for i in cha:
        dic[i] = cha.count(i)
    sett = set(dic)
    lis = sorted(list(sett))

    for i in lis:
        if i.isupper() or i == ' ':
            cha2.append(i)
    print(cha2)
    print(lis, len(cha2))
    lis = lis[len(cha2)::]
    lis.extend(cha2)
    print(lis)

    for i in lis:
        print(i, ':', end=' ')
        for j in range(dic[i]):
            print(('|' if j % 5 == 0 and j != 0 else '')+'-', end='')
        print()
main()
