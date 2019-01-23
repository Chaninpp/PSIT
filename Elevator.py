''' Elevator '''
def main(maxx, start, tier):
    '''
    Ex. input       output
        5           5
        3
        UP
        DOWN
        UP
        UP
        UP
        END
    '''
    while tier != 'END':
        tier = input()
        start += 1 if tier == 'UP' and start < maxx else -1 if tier == 'DOWN' and start > 1 else 0
    return start

print(main(int(input()), int(input()), ''))
