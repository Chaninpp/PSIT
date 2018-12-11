''' Classify '''
def main():
    ''' for '''
    dic = dict()
    while True:
        idem = input()
        if idem == "END":
            break
        if idem[:4] not in dic:
            dic[idem[:4]] = 1
        else:
            dic[idem[:4]] += 1
    year = []
    for i in sorted(dic):
        if i[:2] != year:
            print(i[:2], int(i[2:]), dic[i])
        else:
            print('--', int(i[2:]), dic[i])
        year = i[:2]

main()
