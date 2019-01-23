''' Difference '''
import json
def main(lis_1, lis_2):
    ''' for '''
    dic_1 = {}
    dic_2 = {}
    dic_result = {}
    for i in lis_1:
        dic_1[i] = lis_1.count(i)
    for i in lis_2:
        dic_2[i] = lis_2.count(i)
    print(dic_1, dic_2)
    dic_max = dic_1 if len(dic_1) > len(dic_2) else dic_2
    dic_low = dic_1 if len(dic_1) <= len(dic_2) else dic_2
    for i in dic_max:
        if i in dic_low:
            dic_result[i] = ((dic_max[i] - dic_low[i])*(dic_max[i] > dic_low[i]) + \
                (dic_low[i] - dic_max[i])*(dic_max[i] < dic_low[i]))
    print(dic_result)
main(json.loads(input()), json.loads(input()))