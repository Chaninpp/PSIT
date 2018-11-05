''' Classify '''
def main(dic, result, old_year, old_fac):
    ''' for '''
    while True:
        cha = input()
        if cha == 'END':
            break
        else:
            if int(cha[0:2]) in dic:
                dic[int(cha[0:2])].append(int(cha[2:4]))
            else:
                dic[int(cha[0:2])] = [int(cha[2:4])]
    lis = sorted(list(dic))
    print(dic)
    print(lis)
    for i in lis: # function print
        dic[i] = sorted(dic[i])
        for j in range(len(dic[i])):
            if old_fac != dic[i][j] or i != old_year:
                if str(i) not in result:
                    result.extend([str(i), [str(dic[i][j])+' '+str(dic[i].count(dic[i][j]))]])
                else:
                    result.extend(['--', [str(dic[i][j])+' '+str(dic[i].count(dic[i][j]))]])
                old_fac = dic[i][j]
                old_year = i
                # print(result)
        for j in range(0, len(result), 2):
            print(result[j], *result[j+1])
        result = []

main({}, [], '', '')
