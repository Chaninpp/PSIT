''' Inverter '''
def main(num):
    ''' for Inverter '''
    for i in range(len(num)):
        num[i] = '0' if num[i] == '1' else '1'
    print(int(''.join(num)) if '1' in num else '')

main(list(input()))
