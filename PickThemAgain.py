''' PickThemAgain '''
def main(result):
    ''' for '''
    num = input().split()
    for i in num:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            result.append(i)
    if len(result) > 0:
        print(*result[-1::-1], sep='\n')
    else:
        print('Nope')

main([])
