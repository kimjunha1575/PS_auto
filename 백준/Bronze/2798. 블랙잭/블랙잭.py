N, M = map(int, input().split())
cards = list(map(int, input().split()))
diff = M
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cur = cards[i] + cards[j] + cards[k]
            if cur <= M:
                diff = min(diff, abs(M - cur))
print(M - diff)
