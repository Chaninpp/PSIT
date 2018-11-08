''' BreakPassword '''
import hashlib
def main(cha):
    ''' for '''
    for i in range(100000):
        pas_1 = (hashlib.sha512(str('%05d'%i).encode('utf-8')).hexdigest()).upper()
        if pas_1 == cha:
            print('%05d'%i)
            break
main(input())
