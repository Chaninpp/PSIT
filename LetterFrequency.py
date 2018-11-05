''' LetterFrequency '''
def main(cha):
    ''' for '''

    dic = {}

    for i in cha:
        if i in dic:
            dic[i] += 1
        elif i != ' ':
            dic[i] = 1 # dic = {'L': 1, 'e': 1, 't': 5, 'f': 5}

    max_value = max(dic.values())

    for i in dic:
        if max_value == dic[i]:
            print(i)
main(input().lower().strip('.'))
