''' Sequence I '''
def main():
    ''' for loop '''
    num = int(input())
    for _ in range(num):
        for i in range(1, num+1):
            print(i, end=' ')
        print()

main()
