''' Pick '''
import json
def main():
    ''' for '''
    dic = json.loads(input())
    check = input()
    print('Yes' if check in dic else 'No')
    print(dic[check] if check in dic else '')

main()
