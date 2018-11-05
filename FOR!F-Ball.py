''' FOR!F-Ball '''
def main():
    ''' check ball '''
    cha = input()
    result = [1, 0, 0]
    for i in cha:
        if i == 'A':
            result[0], result[1] = result[1], result[0]
        elif i == 'B':
            result[1], result[2] = result[2], result[1]
        elif i == 'C':
            result[0], result[2] = result[2], result[0]
    print(result.index(1)+1)

main()
