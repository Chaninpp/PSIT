def main1():
    nub = 0
    n = int(input())
    for i in range(n):
        for j in range(i, n):
            print(i, j)
            nub += 1


    print(nub, (n*(n+1))/2)

def main2():
    for i in range(n):
