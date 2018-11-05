''' BootSequence '''
def main():
    ''' for print 1 - num '''
    num = int(input())
    for i in range(1, num):
        print(i, "", sep="_", end="")
    print(num)
main()
