'''
1502 문제 읽고 간단히 구상하면서 입력부분 작성
1503 구상 1 마무리
1505 구현 시작
1515 오픈된 케이스에 대해 정답 확인,제출


구상 1
왼손과 오른손의 위치를 1행 2열 리스트로 트래킹하면서
target 변수의 각 글자에 따라 이동시간과 누르는 데 걸리는 시간을 합치면 정답
두 손을 동시에 움직일 수 없고 한글 자음은 왼손, 한글 모음은 오른손으로만 입력하므로
각 글자의 위치에 따라 움직여야 할 손의 위치부터 눌러야 할 자판의 위치까지의 거리에 1을 더하면
해당 문자를 누르는 데 걸리는 시간이 된다.
각 글자에 따라 이를 전부 누적하면 정답이 될 것.
문자열 최대 100개이므로 시간복잡도에 대한 고민은 크게 하지 않아도 될 듯 함.
'''

def get_dist(frm, to):
    sr, sc = keyboard[frm]
    dr, dc = keyboard[to]
    return abs(sr - dr) + abs(sc - dc)


left, right = input().split()
target = input()
keyboard = dict()
for_left = 'qwertasdfgzxcv'
for_right = 'yuiophjklbnm'
row0 = 'qwertyuiop'
row1 = 'asdfghjkl'
row2 = 'zxcvbnm'
rows = [row0, row1, row2]
for i in range(len(rows)):
    for j in range(len(rows[i])):
        keyboard[rows[i][j]] = (i, j)
ans = 0
for c in target:
    if c in for_left:
        ans += get_dist(left, c) + 1
        left = c
    else:
        ans += get_dist(right, c) + 1
        right = c
print(ans)
