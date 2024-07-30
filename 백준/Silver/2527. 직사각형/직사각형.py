for case in range(4):
    r1, c1, r2, c2, r3, c3, r4, c4 = map(int, input().split())
    if r2 < r3 or c2 < c3 or r4 < r1 or c4 < c1:
        print('d')
    elif (r2, c2) == (r3, c3) or (r4, c4) == (r1, c1) or (r1, c2) == (r4, c3) or (r2, c1) == (r3, c4):
        print('c')
    elif ((r2 == r3 or r1 == r4) and (c3 <= c2 or c1 <= c4)) or ((c2 == c3 or c1 == c4) and (r3 <= r2 or r1 <= r4)):
        print('b')
    else:
        print('a')
