def is_done(r1, c1, r2, c2):
    global cnt_blue
    global cnt_white
    done = True
    color = board[r1][c1]
    # 선택된 구간 중 색이 다른 것이 있으면 done을 False로 변경 후 반복 종료
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if board[r][c] != color:
                done = False
                break
        if not done:
            break
    # done이 True라면 색에 따라 카운트
    if done:
        if color:
            cnt_blue += 1
        else:
            cnt_white += 1
    return done


def solve(r1, c1, r2, c2):
    # 현재 구간에 대해 색종이가 유효한지 검사
    if is_done(r1, c1, r2, c2):
        # 유효하다면 종료
        return
    # 유효하지 않다면 4개의 구간으로 나누어 재귀호출
    rm = (r1 + r2 + 1)//2
    cm = (c1 + c2 + 1)//2
    solve(r1, c1, rm-1, cm-1)
    solve(r1, cm, rm-1, c2)
    solve(rm, c1, r2, cm-1)
    solve(rm, cm, r2, c2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt_white = 0
cnt_blue = 0
solve(0, 0, N-1, N-1)
print(cnt_white)
print(cnt_blue)
