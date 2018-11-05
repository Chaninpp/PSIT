''' LastStand '''
import json
def main():
    ''' for '''
    num = json.loads(input())
    for i in range(len(num)):
        print(num[i]%10)

main()
