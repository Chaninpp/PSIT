"""Boomerang"""
def function():
    """Function's docstring"""
    numx = int(input())
    numy = int(input())
    numz = int(input())
    print(function1(numx))
    print(function2(numy))
    print(function3(numz))
    print(function4(numx, numy))
    print(function5(numx, numy, numz))

def function1(numx):
    """Function1's docstring"""
    result = numx + 1
    return result

def function2(numy):
    """Function2's docstring"""
    result = 7*(numy**3) + 2*(numy**2) - 31*numy + 1
    return result

def function3(numz):
    """Function3's docstring"""
    result = -numz
    return result

def function4(numx, numy):
    """Function4's docstring"""
    result = (numx+numy) * (numx-numy)
    return result

def function5(numx, numy, numz):
    """Function5's docstring"""
    result = (((numy - (((numy**2)-(4*numx*numz))**(1/2)))/(2*numx)))
    return result

function()
