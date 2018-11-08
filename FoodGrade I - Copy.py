""" FoodGrade I """
def checkkai(weight, total, counter):
    """
    Check the chicken that have their weight in range 50 - 70
    and call function itself to check more chicken if counter less than 23
    if not print total chicken that pass

    Args:
        weight  (int): Chicken weight
        counter (int): Counter in
        total   (int): Total pass chicken
    """
    if counter < 23:
        checkkai(int(input()), total + (1 if 50 <= weight <= 70 else 0), counter + 1)
    else:
        print(total + (1 if 50 <= weight <= 70 else 0))

checkkai(int(input()), 0, 0)
""" By it61070200 """