N, K = map(int, input().split())
prices = [int(input()) for _ in range(N)]
prices.sort(reverse=True)
cnt = 0
cur = 0
cur_idx = 0
while cur <= K:
    if cur + prices[cur_idx] <= K:
        cur += prices[cur_idx]
        cnt += 1
        if cur == K:
            break
    else:
        cur_idx += 1

print(cnt)
