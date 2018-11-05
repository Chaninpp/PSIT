""" Safe """
def safe(chest, lock):
    """ find the lowest energy to open chest """
    ans = 0
    for i in range(len(chest)):
        if chest[i] != lock[i]:
            ans += min(abs(ord(chest[i]) - ord(lock[i])), 26-abs(ord(chest[i]) - ord(lock[i])))
    return ans

print(safe(input(), input()))
