"""TheFunctionWithin"""
def func1(num):
    """Function1's"""
    form = 2 * num
    return form

def func2(num):
    """Function2's"""
    form = (3*(num**4)) - (num**3) + (2*(num**2)) + 10
    return form

def func3(numx, numy, numz):
    """Function3's"""
    form = ((numz+numx)**2) - (numx*numy) + (numy**2)
    return form

def func4(numa, numb, numc, numd):
    """Function4's"""
    form = ((numa**2) + (numb**2) - (numc**2)) / ((numd**2) - (2*numa*numd) + (2*numa))
    return form

def main(numa, numb, numc, numd):
    """Function's Main"""
    print(func1(func1(numa)))
    print(func2(func1(numa-numb)))
    print(func3(func1(numa+numb), func1(numa+numc), func2(func1(numd**2))))
    print(func4((func3(func1(numa+numb), func1(numa-numc), func2(func1(numd**2)))),\
     func2(func1(numa-numb)), func1(func1(func1(func1(func1(numc))))), numd**8))

main(float(input()), float(input()), float(input()), float(input()))
