""" Catalan """
def catalan(num):
    """ return catalan of n """
    if num == 1:
        return 1
    else:
        return int((4*(num-1)+2)/(num+1)*catalan(num-1))

print(catalan(int(input())))
