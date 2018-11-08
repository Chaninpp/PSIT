''' Ball '''
def main(height):
    ''' for '''
    nub = 0
    while height > 0.01:
        height *= 0.6
        nub += 1
    return nub - (1 if nub != 0 else 0)
print(main(float(input())))
