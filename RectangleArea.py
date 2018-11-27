''' RectangleArea '''
def main(data_1, data_2):
    '''for RectangleArea'''
    lis = []
    lis.append(list(map(int, data_1.split())))
    lis.append(list(map(int, data_2.split())))
    pos_x1 = lis[0][0] + lis[0][2]
    pos_y1 = lis[0][1] + lis[0][3]
    pos_x2 = lis[1][0] + lis[1][2]
    pos_y2 = lis[1][1] + lis[1][3]
    pointx = min(pos_x1, pos_x2) - max(lis[0][0], lis[1][0])
    pointy = min(pos_y1, pos_y2) - max(lis[0][1], lis[1][1])
    if pointx > 0 and pointy > 0:
        print(pointx*pointy)
    else:
        print("no overlapping")
main(input(), input())
