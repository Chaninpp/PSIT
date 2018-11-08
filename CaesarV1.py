''' CaesarV1 '''
def  main(num, cha, result):
    ''' for Caesar N '''
    for i in cha:
        if not i.isalpha():
            result += i
        else:
            for _ in range(abs(num)):
                if i.isupper():
                    i = '[' if ord(i) == 65 and num < 0 else i
                    i = '@' if ord(i) == 90 and num > 0 else i
                    i = chr(ord(i)+1) if num > 0 else chr(ord(i)-1)
                else:
                    i = '{' if ord(i) == 97 and num < 0 else i
                    i = '`' if ord(i) == 122 and num > 0 else i
                    i = chr(ord(i)+1) if num > 0 else chr(ord(i)-1)
            result += i
    return result

print(main(int(input())%26, input(), ''))
