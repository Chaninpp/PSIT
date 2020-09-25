''' Caesar '''
def shift(cha):
    ''' for Caesar N '''
    result = ''
    for i in cha:
        result += 'a' if i == 'z' else 'A' if i == 'Z' else i if not i.isalpha() else chr(ord(i)+1)
    return result

def main(cha):
    ''' for '''
    lis_word = ['the', 'are', 'there', 'were', 'you']

    for i in range(0, 26):
        for k in range(len(lis_word)):
            if lis_word[k] in cha:
                return (cha, i)
        cha = shift(cha)

print(main(input()))
