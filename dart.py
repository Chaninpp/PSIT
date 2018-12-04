''' dart '''
import math
def main(nub):
    ''' for '''
    for _ in range(int(input())):
        point = input().split()
        pos = math.hypot(int(point[0]), int(point[1]))
        nub += 5 if pos <= 2 else 4 if 2 < pos <= 4 else 3 if 4 < pos <= 6 else 2 \
        if 6 < pos <= 8 else 1 if 8 < pos <= 10 else 0
    return nub

print(main(0))
