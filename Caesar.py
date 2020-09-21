''' Caesar '''
def  main(cha):
    ''' for Caesar N '''
    result = ''
    for i in cha:
        result += 'a' if i == 'z' else 'A' if i == 'Z' else i if not i.isalpha() else chr(ord(i)+1)
    return result

def main2(cha):
    ''' for '''
    lis_word = ['the', 'are', 'is', 'there']

    for i in range(0, 26):
        oldWord = cha
        cha = cha.split()
        for j in cha:
            if j.lower() in lis_word:
                result = oldWord
                return (result, i)
        cha = main(oldWord)

print(main2(input()))
