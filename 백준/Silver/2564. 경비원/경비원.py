width, height = map(int, input().split())
N = int(input())
shops = []
for _ in range(N):
    region, dist = map(int, input().split())
    shops.append((region, dist))
pos = tuple(map(int, input().split()))
ans = 0
if pos[0] == 1:
    for shop in shops:
        if shop[0] == 1:
            ans += abs(pos[1] - shop[1])
        elif shop[0] == 2:
            ans += min(pos[1] + shop[1], 2 * width - (pos[1] + shop[1])) + height
        elif shop[0] == 3:
            ans += pos[1] + shop[1]
        elif shop[0] == 4:
            ans += (width - pos[1]) + shop[1]
elif pos[0] == 2:
    for shop in shops:
        if shop[0] == 1:
            ans += min(pos[1] + shop[1], 2 * width - (pos[1] + shop[1])) + height
        elif shop[0] == 2:
            ans += abs(pos[1] - shop[1])
        elif shop[0] == 3:
            ans += (height - shop[1]) + pos[1]
        elif shop[0] == 4:
            ans += (width - pos[1]) + (height - shop[1])
elif pos[0] == 3:
    for shop in shops:
        if shop[0] == 1:
            ans += pos[1] + shop[1]
        elif shop[0] == 2:
            ans += (height - pos[1]) + shop[1]
        elif shop[0] == 3:
            ans += abs(pos[1] - shop[1])
        elif shop[0] == 4:
            ans += min(pos[1] + shop[1], 2 * height - (pos[1] + shop[1])) + width
elif pos[0] == 4:
    for shop in shops:
        if shop[0] == 1:
            ans += (width - shop[1]) + pos[1]
        elif shop[0] == 2:
            ans += (width - shop[1]) + (height - pos[1])
        elif shop[0] == 3:
            ans += min(pos[1] + shop[1], 2 * height - (pos[1] + shop[1])) + width
        elif shop[0] == 4:
            ans += abs(pos[1] - shop[1])

print(ans)
