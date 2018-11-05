''' Flatten '''
import json
def main(lis, result, lis_temp):
    ''' for Flatten list '''
    lis_temp = lis
    while lis_temp != []:
        lis_temp = []
        for i in lis:
            if isinstance(i, int):
                result.append(i)
            else:
                lis_temp.extend(i)
        lis = lis_temp
    print(sorted(result, reverse=True))

main(json.loads(input()), [], [])
