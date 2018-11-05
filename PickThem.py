''' PickThem '''
import json
def main(result):
    ''' for '''
    num = json.loads(input())
    for i in num:
        if int(i) % 2 == 0:
            result.append(i)
    if len(result) > 0:
        print(*result, sep='\n')
    else:
        print('Nope')

main([])
