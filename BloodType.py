''' BloodType '''
def loop(giver, heir):
    ''' for test case '''
    blood = ['A', 'B', 'AB', 'O']
    RHF = ['-', '+']
    result = []
    for k in RHF:
        for i in blood:
            data = giver+' '+i+k+' '+'?'
            check = main(data.split(), data)
            check = check.replace('{', '').replace('}', '').split()
            if heir in check[2:]:
                result.append(i+k)
    result.sort()
    print(result)
    return result

def start(BloodType):
    ''' function's start '''
    lis_data = BloodType.split()
    if '?' == lis_data[-1]:
        print(main(lis_data, BloodType))
    else:
        if '?' == lis_data[0]:
            result = loop(lis_data[1], lis_data[2])
        else:
            pass
        print(BloodType.replace('?', '{'+' '.join(result)+'}'))

def main(lis_data, BloodType):
    ''' for BloodType '''
    dic = {'A': ['A+', 'A-'], 'B': ['B+', 'B-'], 'AB': ['AB+', 'AB-'], 'O': ['O+', 'O-']}
    RHF = sorted(lis_data[0][-1]+lis_data[1][-1])
    lis_data = sorted([lis_data[0][0:-1], lis_data[1][0:-1]])
    lis_data = sorted(lis_data, key=len)
    if (lis_data[0] == lis_data[1] or lis_data[0] == 'O' or lis_data[1] == 'O') \
    and 'AB' not in lis_data:  # A A ? | B B ? | O A ? | B O ?
        result = same(dic, lis_data, RHF)
    elif lis_data[0] == 'A' or lis_data[0] == 'B':
        result = diff(dic, lis_data, RHF)
    else: # AB+ AB+ ? // AB- AB- ?
        result = [' '.join(dic['A']) if RHF != ['-', '-'] else dic['A'][1]]
        result.append(' '.join(dic['B']) if RHF != ['-', '-'] else dic['B'][1])
        if 'O' not in lis_data:
            result.append(' '.join(dic['AB']) if RHF != ['-', '-'] else dic['AB'][1])
    return BloodType.replace('?', '{'+' '.join(result)+'}')

def same(dic, lis_data, RHF):
    ''' for same '''
    if RHF != ['-', '-']:
        result = sorted(set([" ".join(dic[lis_data[0]])]))
        if lis_data[0] != 'AB' and lis_data[0] != 'O':
            result.append(" ".join(dic['O']))
        elif lis_data[0] != 'O':
            result.append(" ".join(dic['B']))
            result.append(" ".join(dic['A']))
            result.reverse()
    else:
        result = sorted(set([dic[lis_data[0]][1]]))
        if lis_data[0] != 'AB' and lis_data[0] != 'O':
            result.append(dic['O'][1])
        elif lis_data[0] != 'O':
            result.append(dic['B'][1])
            result.append(dic['A'][1])
            result.reverse()
    return result

def diff(dic, lis_data, RHF):
    ''' for different '''
    result = dic[lis_data[0]] if RHF != ['-', '-'] else [dic[lis_data[0]][1]]
    if lis_data[1] == 'B':
        result.append(' '.join(dic['B']) if RHF != ['-', '-'] else dic['B'][1])
        result.append(' '.join(dic['AB']) if RHF != ['-', '-'] else dic['AB'][1])
        result.append(' '.join(dic['O']) if RHF != ['-', '-'] else dic['O'][1])
    elif lis_data[1] == 'AB':
        if lis_data[0] == 'A':
            result.append(' '.join(dic['B']) if RHF != ['-', '-'] else dic['B'][1])
        else:
            result.append(' '.join(dic['A']) if RHF != ['-', '-'] else dic['A'][1])
            result.reverse()
        result.append(' '.join(dic['AB']) if RHF != ['-', '-'] else dic['AB'][1])
    else:
        result.append(' '.join(dic['O']) if RHF != ['-', '-'] else dic['O'][1])
    return result

start(input())
