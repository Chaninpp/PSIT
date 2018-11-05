""" Fizz Buzz """
def main():
    """ input number """
    num = int(input())
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 == 0:
                print("Fizz Buzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
        else:
            print(i)

main()
