N = int(input())

left = 1
right = 1
acc = 1
ans = 0
while left <= right <= N:
    if acc == N:
        ans += 1
        acc -= left
        left += 1
        right += 1
        acc += right
    if acc < N:
        right += 1
        acc += right
    if acc > N:
        acc -= left
        left += 1

print(ans)
