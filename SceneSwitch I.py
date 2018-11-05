''' SceneSwitch I '''
def main():
    ''' count Warmwhite '''
    old = 0
    nub = 0
    count = 0
    color = 'w'
    while True:
        new = input()
        if new == 'End':
            break
        else:
            new = float(new)
            nub += 1 # count open close
            if nub == 3:
                if color == 'w':
                    if new - old <= 6:
                        count += 1
                        color = 'o'
                        nub = 1
                        # print('orange')
                    else:
                        color = 'w'
                        nub = 1
                        # print('white')
                else:
                    color = 'w'
                    nub = 1
                    # print('white')
            # print('---- new - old', new - old, nub)
            old = new
    print(count)

main()
