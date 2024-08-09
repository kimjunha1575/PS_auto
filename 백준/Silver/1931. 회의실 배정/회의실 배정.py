'''
1. 가장 빨리 끝나는 작업을 수행
2. 현재 시간을 방금 수행한 작업의 끝나는 시간으로 갱신
3. 현재 시간 이후로 수행할 수 있는 작업 중 가장 빨리 끝나는 작업을 수행
4. 3~4를 반복
'''


N = int(input())
reservations = []
for _ in range(N):
    st, en = map(int, input().split())
    reservations.append((en, st))
reservations.sort()
cnt = 0
cur_time = 0
for rsv in reservations:
    if rsv[1] < cur_time: continue
    cur_time = rsv[0]
    cnt += 1

print(cnt)