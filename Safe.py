""" Safe """
def safe(chest, lock):
    """ find the lowest energy to open chest """
    nub = 0
    for i in range(len(chest)):
        nub += min(abs(ord(chest[i])-ord(lock[i])), 26-(abs(ord(chest[i])-ord(lock[i]))))
    return nub

print(safe(input(), input()))
