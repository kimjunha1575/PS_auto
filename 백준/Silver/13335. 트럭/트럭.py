def not_done():
    # 마지막 트럭이 다리를 지나기 전까지 True 반환
    return tail < n


def tik():
    global tiktok
    global positions
    global cur_weight
    global head
    global tail
    # skip sequence
    if positions[head] < w - 1 and cur_weight + weights[tail] > L:
        skip = (w-1) - positions[head]
        tiktok += skip
        for truck in range(head, tail):
            positions[truck] += skip
        return None
    # normal sequence
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
            tail += 1
            positions[truck] += 1
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
print(tiktok + w)
