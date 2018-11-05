""" [EX] MissionImImpossible """
def main():
    """ Calculate """
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    nume = int(input())
    numf = int(input())
    numg = int(input())
    numh = int(input())
    numi = int(input())
    numj = int(input())
    numk = int(input())
    numl = int(input())

    det = (((numa * numf * numk) + (numb * numg * numi) + (numc * nume * numj)) -\
    ((numi * numf * numc) + (numj * numg * numa) + (numk * nume * numb)))
    ''' X '''
    total = str(int((((numd * numf * numk) + (numb * numg * numl) + (numc * numh * numj))-\
        ((numl * numf * numc) + (numj * numg * numd) + (numk * numh * numb)))/det))+' '
    ''' Y '''
    total += str(int((((numa * numh * numk) + (numd * numg * numi) + (numc * nume * numl))-\
            ((numi * numh * numc) + (numl * numg * numa) + (numk * nume * numd)))/det))+' '
    ''' Z '''
    total += str(int((((numa * numf * numl) + (numb * numh * numi) + (numd * nume * numj))-\
            ((numi * numf * numd) + (numj * numh * numa) + (numl * nume * numb)))/det))

    print(total) # print X Y Z

main()
