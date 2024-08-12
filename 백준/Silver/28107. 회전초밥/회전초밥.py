import heapq


'''
n번 초밥을 주문한 손님의 목록을 priority queue로 저장
n번 초밥이 완성될 때 마다 가장 앞에 있는 손님이 해당 초밥을 먹는다
'''
N, M = map(int, input().split())
order_lists = [[] for _ in range(200001)]
for customer in range(N):
    orders = list(map(int, input().split()))
    for order in range(1, len(orders)):
        heapq.heappush(order_lists[orders[order]], customer)
foods = list(map(int, input().split()))
ans = [0] * N
for food in foods:
    if order_lists[food]:
        ans[heapq.heappop(order_lists[food])] += 1
print(*ans, sep=' ')
