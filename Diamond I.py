''' Diamond I '''
def main(num):
    ''' for '''
    num_1 = int(input())
    lis = [0]*num_1
    for _ in range(num):
        lis_t = [int(i) for i in input().split()]
        lis = [lis[i] + lis_t[i] for i in range(num_1)]
    print(max(lis))
main(int(input()))
