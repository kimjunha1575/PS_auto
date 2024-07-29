N = int(input())
sticks = []
for _ in range(N):
    sticks.append(int(input()))
cur_max = 0
ans = 0
for stick in sticks[-1::-1]:
    if stick > cur_max:
        cur_max = stick
        ans += 1
print(ans)
