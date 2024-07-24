def not_done():
    # 마지막 트럭이 다리를 지나기 전까지 True 반환
    return positions[n-1] <= w


def tik():
    global tiktok
    global positions
    global cur_weight
    global head
    global tail
    tiktok += 1
    targets = range(head, tail + 1)
    for truck in targets:
        if truck >= n:
            break
        if 1 <= positions[truck] <= w:
            positions[truck] += 1
            if positions[truck] > w:
                head += 1
                cur_weight -= weights[truck]
        if positions[truck] == 0 and cur_weight + weights[truck] <= L:
            cur_weight += weights[truck]
            # Can occur oob error
            tail += 1
            positions[truck] += 1

    # 다리에 이미 진입한 트럭
        # 매 틱마다 1칸씩 전진
        # 다리를 빠져나가면 제한하중에서 해당 트럭 무게 제외
    # 다리에 진입하지 못한 트럭(대기중인 트럭은 선두만 고려해도 됨)
        # 다리에 진입 가능하면 바로 진입
    # head: 다리를 '건너고 있는' 트럭 중 선두의 인덱스
    # tail: '대기하고 있는' 트럭 중 선두의 인덱스
    return None


def solve():
    while not_done():
        tik()
    return None


n, w, L = map(int, input().split())
weights = list(map(int, input().split()))
positions = [0] * n
tiktok = 0
cur_weight = 0
head = 0
tail = 0
solve()
print(tiktok)
