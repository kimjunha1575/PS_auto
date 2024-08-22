'''
1553 문제 읽기 시작
1555 설계 시작
이해한 바로는 '탐사선'은 고정되어 있고, 고정된 위치에서 어떤 방향으로 신호를 보내야
신호가 가장 오래 항성계 내부에 존재하는 지 판단하는 문제
무한히 존재할 수 있다면 다른 출력 -> visited배열로 이미 왔던 곳에 다시 온다면 무한히 존재할 것으로 판단(순환하는 경로)
각 방향에 따라 행성의 종류에 따라 굴절되는 방향이 다른데,
종류에 따라 배열로 저장해두고 쓰면 편리할 듯 함
행성계 밖으로 나가거나, 블랙홀을 만나면 시그널이 사라진다.
4가지 방향 중 시그널이 순회한 칸이 가장 많은 경우의 방향과 칸의 개수를 출력
무한히 있을 수 있다면 다른 문자열 출력

방향 누적해가면서 그래프 순회
행성계 최대 크기 500 * 500
행성계 당 최대 4번이므로 완전탐색 가능

1558 구현 시작
1631 구현완료, 예제에 대해 정답 확인, 제출 -> 오답
1639 순회한 칸 수에 처음 위치를 포함하는 방식으로 변경, 제출 -> 오답
1642 무한히 순회할 수 있는 경우에도 방향에 따른 우선순위가 있음 -> 제출, 정답
'''

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
RU = [3, 2, 1, 0]
LU = [1, 0, 3, 2]
height, width = map(int, input().split())
board = [list(input()) for _ in range(height)]
pr, pc = map(int, input().split())
cur_max = 0
can_go_infinitely = False
infinite_dir = None
ans = []
ans_infinites = []
ans_priority = [3, 0, 1, 2]
dir_to_str = ['R', 'D', 'L', 'U']
for start_dir in range(4):
    cnt = 1
    cur_dir = start_dir
    cr, cc = pr - 1, pc - 1
    visited = [[[0] * width for _ in range(height)] for _ in range(4)]
    while True:
        nr = cr + DIRECTIONS[cur_dir][0]
        nc = cc + DIRECTIONS[cur_dir][1]
        if not (0 <= nr < height and 0 <= nc < width): break
        if board[nr][nc] == 'C':
            break
        if visited[cur_dir][nr][nc]:
            can_go_infinitely = True
            ans_infinites.append(start_dir)
            break
        if board[nr][nc] == '.':
            visited[cur_dir][nr][nc] = 1
            cr = nr
            cc = nc
            cnt += 1
            continue
        if board[nr][nc] == '/':
            visited[cur_dir][nr][nc] = 1
            cur_dir = RU[cur_dir]
            cr = nr
            cc = nc
            cnt += 1
            continue
        else:
            visited[cur_dir][nr][nc] = 1
            cur_dir = LU[cur_dir]
            cr = nr
            cc = nc
            cnt += 1
            continue
    ans.append((start_dir, cnt))

if can_go_infinitely:
    for i in ans_priority:
        if i in ans_infinites:
            print(dir_to_str[i])
            break
    print("Voyager")
else:
    cur_ans = -1
    cur_ans_dir = 0
    possible_answers = []
    for result in ans:
        if result[1] > cur_ans:
            cur_ans = result[1]
            possible_answers = [result]
        elif result[1] == cur_ans:
            possible_answers.append(result)
    if len(possible_answers) > 1:
        done = False
        for i in ans_priority:
            for ans in possible_answers:
                if i == ans[0]:
                    done = True
                    print(dir_to_str[ans[0]])
                    print(ans[1])
            if done:
                break
    else:
        print(dir_to_str[possible_answers[0][0]])
        print(possible_answers[0][1])
