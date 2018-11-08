''' Password '''
import hashlib
def main(cha):
    ''' for '''
    print((hashlib.sha512(cha.encode('utf-8')).hexdigest()).upper())
main(input())
