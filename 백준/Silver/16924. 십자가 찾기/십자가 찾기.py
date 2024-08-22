'''
1527 문제 읽고 입력 코드 작성
1528 구상 1 시작
1535 구상 1 끝 구현시작
1551 구현 끝, 오픈된 테케에서 의도하지 않은 답이 포함되는 것 확인, 디버깅 시작
1554 십자가를 펼쳐나갈 때 더해지는 좌표값에 size를 곱하지 않았음을 확인, 수정
1555 *을 만나면 즉시 cnt에서 1을 빼는 부분에서 오류가 남을 확인, 수정시작
1557 해당 코드의 위치를 유효성 확인 이후로 옮기고 오픈된 모든 테케에서 정답 확인, 제출 -> 오답
1601 최대 십자가의 개수 M*N 조건 때문인 것으로 판단, 수정시작
1607 같은 자리에서 최대크기의 십자가만 리스트에 추가되도록 변경, 십자가 개수가 N*M을 넘어가면 -1을 출력하도록 변경, 제출 -> 오답
1611 십자가 개수 출력 빼먹은 것 확인, 수정 후 제출




구상 1
M, N이 100이하
십자가가 겹쳐도 되므로 *을 없애가는 방식으로는 하면 안됨
board는 유지하되, 십자가로 덮어야 하는 상태인지 아닌지 체크 필요
맵 크기 100 * 100
십자가가 맵 바깥에 걸치게 되는 경우는 문제 조건 상 없는 것 같으므로
십자가의 최대 크기는 50(49이긴 함)
총 1만개의 점에 대해 크기 1부터 50까지의 십자가를 모두 대입해봐도
시간 안에 해결 가능할 듯 함
점을 이동할 때 마다 남아있는 십자가를 덮어야 하는 점이 있는 지 확인하고
없다면 지금까지의 십자가 대입 결과를 출력하면 정답일 것.
++ 1542 덮어야 하는 별의 개수를 카운트하면서 0이 되면 break 하는 방식이 더 빠를 듯
'''

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
height, width = map(int, input().split())
board = [input() for _ in range(height)]
done = [[0] * width for _ in range(height)]
crosses = []
cnt = 0
for r in range(height):
    for c in range(width):
        if board[r][c] == '*':
            cnt += 1
for r in range(1, height - 1):
    all_done = False
    for c in range(1, width - 1):
        if board[r][c] == '.': continue
        can_put_cross = False
        max_size = min(r, c, height - 1 - r, width - 1 - c)
        size = 1
        while size <= max_size:
            valid = True
            targets = []
            for dr, dc in directions:
                nr = r + dr * size
                nc = c + dc * size
                if not (0 <= nr < height and 0 <= nc < width):
                    valid = False
                    break
                if board[nr][nc] != '*':
                    valid = False
                    break
                targets.append((nr, nc))
            if valid:
                can_put_cross = True
                for row, col in targets:
                    if done[row][col] == 0:
                        done[row][col] = 1
                        cnt -= 1
            else:
                break
            if done[r][c] == 0:
                done[r][c] = 1
                cnt -= 1
            if cnt == 0:
                all_done = True
            size += 1
        if can_put_cross:
            crosses.append((r + 1, c + 1, size - 1))
            if len(crosses) > height * width:
                all_done = True
                crosses = []
                break
    if all_done:
        break

if crosses and cnt == 0:
    print(len(crosses))
    for cross in crosses:
        print(*cross, sep=' ')
else:
    print(-1)

