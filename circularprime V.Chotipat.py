"""
CircularPrime
"""
def sum_circular_prime(num):
    """Return sum of circular prime from 1 to num"""
    total = 0
    for i in range(1, num+1):
        if is_circular_prime(i):
            total = total + i
    return total
  
def is_circular_prime(num):
    """Return True if num is circular prime else otherwise"""
    for i in range(len(str(num))): 
        rotate_num = rotate(num, i)
        if not is_prime(rotate_num):
            return False
    return True
  
def rotate(num, i):
    """Return number by rotating i digit"""
    num = str(num)
    num = num[i:] + num[:i]
    return int(num)
  
def is_prime(num):
    """Return True if num is prime else otherwise"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
  
print(sum_circular_prime(int(input())))
