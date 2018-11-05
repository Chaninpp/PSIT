''' Divide3Or5 '''
def main():
    ''' check number 1-n if i%3=0 or i%5=0 result += i '''
    num = int(input())
    result = 0
    for i in range(1, num+1):
        if i%3 == 0 or i%5 == 0:
            result += i
    print(result)

main()
