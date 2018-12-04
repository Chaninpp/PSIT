''' TicTacToe '''
def main(line):
    ''' for '''
    winx, wino = 'XXX', 'OOO'
    temp = ['', '']
    for i in range(3):
        temp[0] += line[i][i]
        temp[1] += line[i][-1-i]
        check = line[0][i]+line[1][i]+line[2][i]
        if line[i] == winx or line[i] == wino:
            return 'O WIN' if line[i] == wino else 'X WIN'
        elif check == winx or check == wino:
            return 'O WIN' if check == wino else 'X WIN'
        elif winx in temp or wino in temp:
            return 'O WIN' if wino in temp else 'X WIN'
    return 'DRAW'

print(main([input(), input(), input()]))
