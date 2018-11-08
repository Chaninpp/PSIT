''' Kabata '''
def main(result):
    ''' for '''
    for _ in range(int(input())):
        cha = input()
        cha_temp = cha.replace('bakka', '').replace('ka', '').replace('ta', '').replace('ba', '')
        result.append('yes' if cha_temp == '' and 'baka' not in cha else 'no')
    print(*result, sep='\n')
main([])
