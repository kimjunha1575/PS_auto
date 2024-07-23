def put_paper(board, paper_cnt, row, col, width, height, paper_num):
    for r in range(row, row + height):
        for c in range(col, col + width):
            if board[r][c] is not None:
                paper_cnt[board[r][c]] -= 1
            board[r][c] = paper_num
            paper_cnt[paper_num] += 1
    return None


board = [[None for _ in range(1001)] for _ in range(1001)]
N = int(input())
paper_cnt = [0 for _ in range(N)]
paper_num = 0
for paper in range(N):
    c, r, width, height = map(int, input().split())
    put_paper(board, paper_cnt, r, c, width, height, paper_num)
    paper_num += 1
for paper in paper_cnt:
    print(paper)
