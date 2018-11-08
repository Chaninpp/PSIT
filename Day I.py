''' Day I '''
def main():
    ''' for calculate leap year '''
    years = int(input())
    if years % 4 == 0:
        if years % 100 == 0:
            if years %400 == 0:
                print('Yes')
            else:
                print('No')
        else:
            print('Yes')
    else:
        print('No')

main()
