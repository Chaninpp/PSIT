''' Antenna '''
import json
def main(radius):
    ''' for '''
    nub = 1
    lis = sorted(json.loads(input()))
    if lis != []:
        scope = lis[0] + radius
        for i in range(len(lis)):
            if lis[i] <= scope:
                pass
            else:
                scope = lis[i] + radius
                nub += 1
        print(nub)
    else:
        print(0)
main(int(input())*2)
