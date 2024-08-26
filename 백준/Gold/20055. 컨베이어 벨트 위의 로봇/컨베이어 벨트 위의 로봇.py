'''
3조 핵심 아이디어

내구도 정보와 로봇 위치를 배열로 저장하고
다른 자료구조 없이 인덱싱으로 접근함
올리는 자리의 인덱스: start
내리는 자리의 인덱스: end
'''

N, K = map(int, input().split())
durations = list(map(int, input().split()))
robots = [0] * N
belt_length = N << 1
start = 0
end = N - 1
step = 0
cnt = 0

# 내구도 0인 칸의 개수가 K개 이상이면 종료
while cnt < K:
    step += 1
    # 벨트 한 칸 회전
    start = (start + belt_length - 1) % belt_length
    end = (end + belt_length - 1) % belt_length
    # 로봇 이동
    for i in range(N-2, -1, -1):
        robots[i+1] = robots[i]
    robots[0] = 0
    # 내리는 위치에 있는 로봇 내리기
    robots[-1] = 0
    # 먼저 올라간 로봇부터 한칸 이동할 수 있다면 이동
    for i in range(N-2, -1, -1):
        if robots[i] == 0: continue
        idx = (start + i) % belt_length
        nxt_idx = (idx + 1) % belt_length
        if durations[nxt_idx] and robots[i+1] == 0:
            robots[i] = 0
            robots[i+1] = 1
            durations[nxt_idx] -= 1
            if durations[nxt_idx] == 0:
                cnt += 1
    robots[-1] = 0
    # 올리는 칸의 내구도가 0이 아니면 로봇 올리기
    if durations[start]:
        robots[0] = 1
        durations[start] -= 1
        if durations[start] == 0:
            cnt += 1

print(step)
