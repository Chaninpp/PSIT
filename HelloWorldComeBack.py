''' HelloWorldComeBack '''
def main():
    ''' check Language '''
    cha = input()
    cha_c = cha.lower()
    if cha_c.islower():
        print('Hello', cha+'.')
    else:
        print('สวัสดี', cha)

main()
