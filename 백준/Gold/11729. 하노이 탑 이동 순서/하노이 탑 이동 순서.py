'''
N개를 전부 p번에서 q번으로 옮기는 방법
1 ~ N-1번을 빈 곳으로 옮긴다
5번을 q번으로 옮긴다
1 ~ N-1번을 q번으로 옮긴다
'''


def solve(n, st, de):
    global K
    if n == 1:
        # 한 층은 그냥 옮긴다
        K += 1
        moves.append((st, de))
        return
    if st != 1 and de != 1: tmp = 1
    elif st != 2 and de != 2: tmp = 2
    else: tmp = 3
    # 맨 아래층을 제외한 n-1층을 st에서 tmp로 옮긴 뒤
    solve(n-1, st, tmp)
    # 맨 아래층을 st에서 de로 옮기고
    K += 1
    moves.append((st, de))
    # tmp에 옮겨뒀던 n-1층의 탑을 de로 다시 쌓는다
    solve(n-1, tmp, de)


N = int(input())
K = 0
# 총 움직인 회수를 먼저 출력한 다음 움직임을 출력해야하므로 배열에 일단 저장
moves = []
# N층의 탑을 1번 장대에서 3번 장대로 옮긴다
solve(N, 1, 3)
print(K)
for st, de in moves:
    print(st, de)
