N = int(input())
M = int(input())
thumbs = list(map(int, input().split()))
cands = [None] + [[0, 0] for _ in range(100)]
pictures = [None for _ in range(N)]

cnt = 0
for i in range(len(thumbs)):
    thumb = thumbs[i]
    # 기존 후보
    if cands[thumb][0]:
        cands[thumb][0] += 1
    # 새로운 후보, 빈자리 없음
    elif cnt == N:
        lowest = 1001
        lowest_idx = 1001
        for j in range(N):
            cur = cands[pictures[j][0]][0]
            cur_idx = pictures[j][1]
            if cur < lowest or (cur == lowest and cur_idx < lowest_idx):
                lowest = min(lowest, cur)
                lowest_idx = pictures[j][1]
                lowest_cand = pictures[j][0]
        cands[thumb][0] += 1
        cands[thumb][1] = cands[lowest_cand][1]
        pictures[cands[lowest_cand][1]] = [thumb, i]
        cands[lowest_cand][0] = 0
        cands[lowest_cand][1] = 0
    # 새로운 후보, 빈자리 있음
    else:
        cnt += 1
        for j in range(N):
            if pictures[j] is None:
                pictures[j] = [thumb, i]
                cands[thumb][0] += 1
                cands[thumb][1] = j
                break

for i in range(N-1, -1, -1):
    if pictures[i] is None:
        del pictures[i]
pictures.sort()
for cand in pictures:
    if cand is not None:
        print(cand[0], end=' ')
