''' Heads and Legs '''
def main(animal, legs):
    ''' Find Legs '''
    cal_bird = legs//2
    if animal == 0 and legs == 0:
        print(0, 0)
    elif (legs//4) > animal:
        print('Impossible')
    elif cal_bird >= animal and legs % 2 == 0 and animal > 0:
        var = ((cal_bird-animal)*2)
        bird = cal_bird-var
        rabbit = cal_bird-animal
        print(rabbit, bird)
    else:
        print('Impossible')
main(int(input()), int(input()))
