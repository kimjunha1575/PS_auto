
def valid():
    for result in results:
        validity = True
        for i in range(18):
            if res[i] > result[i]:
                validity = False
                break
        if validity:
            return True
    return False


def solve(idx):
    if not valid():
        return
    if idx == 15:
        for i in range(4):
            validity = True
            for j in range(18):
                if res[j] != results[i][j]:
                    validity = False
                    break
            if validity:
                valid_results.append(i)
        return
    for i in range(3):
        team1 = team_match[idx][0]
        team2 = team_match[idx][1]
        if i == 0:
            res[team1*3 + 0] += 1
            res[team2*3 + 2] += 1
        elif i == 1:
            res[team1*3 + 2] += 1
            res[team2*3 + 0] += 1
        elif i == 2:
            res[team1*3 + 1] += 1
            res[team2*3 + 1] += 1
        solve(idx + 1)
        if i == 0:
            res[team1*3 + 0] -= 1
            res[team2*3 + 2] -= 1
        elif i == 1:
            res[team1*3 + 2] -= 1
            res[team2*3 + 0] -= 1
        elif i == 2:
            res[team1*3 + 1] -= 1
            res[team2*3 + 1] -= 1

cnt = 0
buf = []
team_match = []
results = [list(map(int, input().split())) for _ in range(4)]
res = [0] * 18
valid_results = []
for i in range(5):
    for j in range(i+1, 6):
        team_match.append((i, j))
solve(0)
for i in range(4):
    if i in valid_results:
        print(1, end=' ')
    else:
        print(0, end=' ')
print()
