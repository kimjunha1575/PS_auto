def getScore(r, a):
    rscore = 0
    ascore = 0
    for i in range(11):
        if r[i] == a[i] == 0:
            continue
        elif r[i] > a[i]:
            rscore += 10 - i
        else:
            ascore += 10 - i
    return rscore - ascore
            
maxScore = 0
answer = [0] * 11

def selectScore(cur, n, cnt, score, target, used, ascore, info):
    global maxScore
    global answer
    ryanScore = [used[i] * target[i] for i in range(11)]
    gap = getScore(ryanScore, info)
    if gap > maxScore:
        maxScore = gap
        answer = [x for x in ryanScore]
    for i in range(cur, -1, -1):
        if used[i]: continue
        nxt = cnt + target[i]
        if nxt > n: continue
        used[i] = 1
        selectScore(i - 1, n, nxt, score + 10 - i, target, used, ascore, info)
        used[i] = 0

def solution(n, info):
    target = [x + 1 for x in info]
    used = [0] * 11
    ascore = 0
    for i in range(11):
        if info[i]:
            ascore += 10 - i
    selectScore(10, n, 0, 0, target, used, ascore, info)
    if sum(answer) < n:
        answer[-1] += n - sum(answer)
    if maxScore > 0:
        return answer
    return [-1]


"""
총점이 최대 55점
어피치의 최대 점수는 정해져 있음



"""