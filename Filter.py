''' Filter '''
import json
def main(result):
    ''' for '''
    check = json.loads(input())
    key = float(input())
    for i in check:
        if key < check[i]: # i = key , check = value
            result[int(i)] = ('%.2f')%check[i]
    key = sorted(result)
    if key == []:
        print('Nope')
    for i in key:
        print(str(i)+'\t'+str(result[i]))

main({})
