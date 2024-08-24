N = int(input())
pc, pr = map(int, input().split())
first_penetration_upward = None
idx = 0
targets = []
for _ in range(N - 1):
    c, r = map(int, input().split())
    if pr < 0 < r:
        if first_penetration_upward is None:
            first_penetration_upward = True
        targets.append([c, idx // 2])
        idx += 1
    elif pr > 0 > r:
        if first_penetration_upward is None:
            first_penetration_upward = False
            idx += 1
        targets.append([c, idx // 2])
        idx += 1
    pr = r
    pc = c

if len(targets) % 2:
    if not first_penetration_upward:
        # print("not upward, penetration not full")
        targets.append([pc, 0])
    else:
        # print("upward, penetration not full")
        targets.append([pc, idx // 2])
else:
    if not first_penetration_upward:
        # print("not upward, penetration full")
        targets[-1][1] = 0
    # else:
        # print("upward, penetration full")

# print(targets)
targets.sort()
# print(targets)
include_other = [0] * (idx // 2 + 1)

ans1 = 0
ans2 = 0

stk = []
for target in targets:
    idx = target[1]
    # print(target, idx)
    if stk:
        if stk[-1] == idx:
            stk.pop()
            if not include_other[idx]:
                ans2 += 1
        else:
            include_other[stk[-1]] = 1
            stk.append(idx)
    elif not stk:
        stk.append(idx)
        ans1 += 1
# print(include_other)

if stk:
    last = stk.pop()
    if not include_other[last]:
        ans2 += 1

print(ans1, ans2)
