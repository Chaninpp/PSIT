''' LastStand '''
def main(num_a, num_b, lis, ris):
    """ main """
    for _ in range(num_a):
        num = int(input())
        lis.append(num)
        lis.sort()
    for _ in range(num_b):
        num = int(input())
        ris.append(num)
    for i in lis:
        if i not in ris:
            print(i, end=' ')
main(int(input()), int(input()), [], [])
