''' Seeker '''
def main(cha, lis, num):
    ''' for
    Ex. IAM503ROT8OOSS001LKFD010LLASD123 = 645
    '''
    for i in cha:
        if i.isnumeric():
            num += i
        else:
            lis.append(int(num))
            num = '0'
    print(sum(lis))

main(input()+'a', [], '0')
