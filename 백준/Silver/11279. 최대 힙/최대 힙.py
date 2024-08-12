import heapq


'''
python의 heapq는 기본적으로 min-heap만 지원하기 때문에
max-heap을 사용하려면 넣는 값의 부호를 뒤집어서 push 한 뒤
사용할 때 다시 뒤집어주면 된다
'''
N = int(input())
pq = []
commands = []
for _ in range(N):
    commands.append(int(input()))
for command in commands:
    if command:
        heapq.heappush(pq, -command)
    elif len(pq):
        print(-heapq.heappop(pq))
    else:
        print(0)
