def solve(n, prev):
    global ans
    if ans == N:
        return
    if n == K:
        res = 0
        for word in words:
            can_read = True
            for char in word:
                if char not in buf:
                    can_read = False
                    break
            if can_read:
                res += 1
        ans = max(ans, res)
        return
    for i in range(prev + 1, 26):
        if learnt[i]: continue
        learnt[i] = 1
        buf.add(letters[i])
        solve(n+1, i)
        buf.discard(letters[i])
        learnt[i] = 0


N, K = map(int, input().split())
words = [input() for _ in range(N)]
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    ans = 0
    letters = [chr(ord('a') + i) for i in range(26)]
    buf = set()
    learnt = [0] * 26
    for i in range(N):
        words[i] = words[i][4:-4]

    # 기본적으로 들어가는 글자에 대한 사전작업
    defaults = "antic"
    for letter in defaults:
        learnt[ord(letter) - ord('a')] = 1
        buf.add(letter)
    K -= 5

    solve(0, 0)
    print(ans)
