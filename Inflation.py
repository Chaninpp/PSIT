''' Inflation '''
def main():
    ''' for calculate inflation 3.81%'''
    num = int(float(input())*100)
    loop = int(input())
    for _ in range(loop):
        num = int(num)
        num *= 10381 # num + num*3.81/100 from 1.0381 * 10000
        num //= 10000
    print('%d.%02d'%((num//100), num%100))

main()
