def solve(cnt, acc, prev):
    global cur_best
    if acc + largest_gap * (N-cnt) < cur_best:
        return
    if cnt == N:
        cur_best = max(cur_best, acc)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        solve(cnt + 1, acc + abs(arr[i] - prev), arr[i])
        used[i] = 0


N = int(input())
arr = list(map(int, input().split()))
cur_best = 0
used = [0] * N
arr.sort()
largest_gap = arr[N-1] - arr[0]
arranged = [0] * N
arranged[0] = arr[N//2 - 1]
arranged[N-1] = arr[N//2]
for i in range(0, N//2-1):
    arranged[2*(i+1)] = arr[i]
for i in range(N-1, N//2, -1):
    arranged[2*(N-i-1)+1] = arr[i]
arr = arranged
for i in range(N):
    used[i] = 1
    solve(1, 0, arr[i])
    used[i] = 0
print(cur_best)
