''' Temperature '''
def main(temp, old, new):
    ''' for '''
    if old == 'C':
        temp_c = temp
        result = ((temp_c * 9 / 5) + 32) if new == 'F' else (temp_c + 273.15) if new == 'K' \
        else ((temp_c + 273.15) * 9 / 5) if new == 'R' else temp
    elif old == 'F':
        temp_c = (temp - 32) * 5 / 9
        result = temp_c if new == 'C' else (temp_c + 273.15) if new == 'K' else \
        ((temp_c + 273.15) * 9 / 5) if new == 'R' else temp
    elif old == 'K':
        temp_c = temp - 273.15
        result = temp_c if new == 'C' else ((temp_c * 9 / 5) + 32) if new == 'F' \
        else ((temp_c + 273.15) * 9 / 5) if new == 'R' else temp
    elif old == 'R':
        temp_c = (temp * 5 / 9) - 273.15
        result = temp_c if new == 'C' else ((temp_c * 9 / 5) + 32) if new == 'F' \
        else ((temp_c + 273.15)) if new == 'K' else temp
    return result
print('%.2f'%(main(float(input()), input(), input())))
