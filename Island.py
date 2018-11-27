''' Island '''
def island(islandmap, row_n, col_n):
    """ island function """
    if islandmap[row_n][col_n] == "1":
        size_x = len(islandmap)
        size_y = len(islandmap[0])
        islandmap[row_n][col_n] = "0"
        # 8-direction
        row_u, row_d = max(0, row_n-1), min(row_n+1, size_x-1)
        col_l, col_r = max(0, col_n-1), min(col_n+1, size_y-1)
        for i in [row_u, row_n, row_d]:
            for j in [col_l, col_n, col_r]:
                island(islandmap, i, j)
        return 1

def main():
    """ main function """
    row, col = input().split()
    row = int(row)
    ans = int(col)*0
    islandmap = [input().split() for _ in range(row)]
    for i in range(row):
        while islandmap[i].count("1") != 0:
            ans += island(islandmap, i, islandmap[i].index("1"))
    print(ans)

main()
