''' Quardrant '''
def main(numx, numy):
    ''' for '''
    print('Y' if numx == 0 and numy != 0 else 'X' if numy == 0 and numx != 0 \
    else 'O' if numx == 0 and numy == 0 else 'Q1' if numx > 0 and numy > 0 else 'Q2' \
    if numx < 0 and numy > 0 else 'Q3' if numx < 0 and numy < 0 else 'Q4')
main(int(input()), int(input()))
