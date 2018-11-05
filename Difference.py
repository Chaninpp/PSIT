''' Difference '''
def main(group_1, group_2, num1, num2):
    ''' for '''
    for _ in range(num1):
        group_1.add(int(input()))
    for _ in range(num2):
        group_2.add(int(input()))
    result = group_1-group_2
    result = tuple(result)
    result = sorted(result)
    print(*result)
main(set(), set(), int(input()), int(input()))
