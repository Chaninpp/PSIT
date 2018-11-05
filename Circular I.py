''' Circular I '''
def main():
    ''' input finction '''
    me_x = float(input())
    me_y = float(input())
    rad = float(input())
    mos_x = float(input())
    mos_y = float(input())
    print('Yes' if ((me_x - mos_x)**2+(me_y - mos_y)**2)**0.5 <= rad else 'No')

main()
