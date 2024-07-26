hor = []
ver = []
width, height = map(int, input().split())
cut = int(input())
for _ in range(cut):
    di, pos = map(int, input().split())
    if di:
        ver.append(pos)
    else:
        hor.append(pos)

hor.sort()
ver.sort()
max_width = width
max_height = height
if len(ver):
    max_width = max(ver[0], width - ver[-1])
    for p in range(1, len(ver)):
        max_width = max(max_width, ver[p] - ver[p-1])
if len(hor):
    max_height = max(hor[0], height - hor[-1])
    for p in range(1, len(hor)):
        max_height = max(max_height, hor[p] - hor[p-1])

print(max_width * max_height)
