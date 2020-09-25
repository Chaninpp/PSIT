''' CaesarV1 '''
def shift(cha):
    ''' for Caesar N '''
    result = ''
    for i in cha:
        result += 'a' if i == 'z' else 'A' if i == 'Z' else i if not i.isalpha() else chr(ord(i)+1)
    return result

def main(num, cha):
    ''' for Caesar N '''
    for _ in range(abs(num)):
        cha = shift(cha)
    return cha

print(main(int(input())%26, input()))

# text = input()
# for i in range(26):
#     print(main(i+1, text, ''))
