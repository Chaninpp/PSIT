''' LineSorting '''
def main():
    ''' - (input) -                 - (output) -
        4
        short line                  single
        longer line                 short line
        this is the longest line    longer line
        single                      this is the longest line
    '''
    cha = [input() for _ in range(int(input()))]
    print(*(sorted(cha, key=len)), sep='\n')

main()
