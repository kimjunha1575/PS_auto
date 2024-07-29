N = int(input())
M = int(input())
votes = list(map(int, input().split()))
candidates = [None] + [[0, 0] for _ in range(100)]
pictures = [None for _ in range(N)]

cnt = 0
for i in range(len(votes)):
    thumb = votes[i]
    if candidates[thumb][0]:
        candidates[thumb][0] += 1
    elif cnt == N:
        lowest_vote = M+1
        lowest_idx = M+1
        lowest_cand = 0
        for j in range(N):
            cur = candidates[pictures[j][0]][0]
            cur_idx = pictures[j][1]
            if cur < lowest_vote or (cur == lowest_vote and cur_idx < lowest_idx):
                lowest_vote = cur
                lowest_idx = pictures[j][1]
                lowest_cand = pictures[j][0]
        candidates[thumb][0] += 1
        candidates[thumb][1] = candidates[lowest_cand][1]
        pictures[candidates[lowest_cand][1]] = [thumb, i]
        candidates[lowest_cand][0] = 0
        candidates[lowest_cand][1] = 0
    else:
        cnt += 1
        for j in range(N):
            if pictures[j] is None:
                pictures[j] = [thumb, i]
                candidates[thumb][0] += 1
                candidates[thumb][1] = j
                break

pictures.sort(key=lambda x: x or [M+1, M+1])
for cand in pictures:
    if cand is not None:
        print(cand[0], end=' ')
