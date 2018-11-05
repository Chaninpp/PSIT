''' Grade II '''
def main():
    ''' calculate score '''
    num = float(input())
    print((chr(70-((num > 64)*2)-(num > 74)-(num > 84)-(num > 94))+('+'*(num%10 < 5)*\
        (59 < num < 100)))*(0 <= num < 101)+('ERR' if num < 0 or num > 100 else ''))

main()
