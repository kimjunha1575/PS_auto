import heapq


'''
파이썬에서 정렬 기준을 정하는 데 여러 방법이 있지만
tuple의 앞쪽 원소로 정렬 순서를 제시하는 것도 방법 중 하나
(이후 사용할 땐 실제 데이터 부분을 꺼내서 쓰면 됨)
'''
N = int(input())
commands = [int(input()) for _ in range(N)]
pq = []
for command in commands:
    if command:
        heapq.heappush(pq, (abs(command), command)) # 절댓값이 작은 순서로 정렬
    elif pq:
        print(heapq.heappop(pq)[1]) # 데이터만 꺼내서 사용
    else:
        print(0)

