'''
1432 1번문제 읽기시작
2차원 배열에서의 완전탐색
배열 크기 최대 50 * 50, 명령 회수 최대 100
다만 배열 밖으로 나가면 반대쪽으로 나오도록 연결해야하고
절차에 따라 구현 + 상태체크 필요
시간복잡도에 대한 고민은 크게 하지 않아도 될 듯 함


1436 2번문제 읽기시작
2N 크기의 1차배열에서 올리는 위치와 내리는 위치를 투포인터처럼 움직이면서
단계별 시뮬레이션 구현

1440 난이도 차이 크게 느껴지지 않으나 구현 조건이 2번이 더 간단해보이므로 2번 풀이 시작
구상 1
2N 크기의 1차배열을 선언한 뒤 올리는 위치, 내리는 위치의 인덱스를 옮겨가면서 단계 진행
단계가 넘어갈 때 마다 올리는 위치와 내리는 위치의 인덱스를 1 씩 빼준다(컨베이어 벨트 진행)
나머지는 문제에 제시된 그대로 진행
1453 간단히 구현 완료(디테일한 부분 아직 고려 안함), 예제 테스트, 인덱스에러
1457 다른 인덱스에러까지 확인 후 에러는 아니지만 오답 출력. 디버깅 시작
(인덱싱이 의심스러움)
벨트가 한 칸 이동하면서 시작하는게 맞는지..?? 맞는거였음
1518 수정 후 예제에 대해 정답 확인, 제출

'''

N, K = map(int, input().split())
arr = list(map(int, input().split()))
occupied = [0] * N
start = 0
end = N - 1
step = 0
cnt = arr.count(0)

while True:
    step += 1
    # 벨트 한 칸 회전
    start = (start + 2*N - 1) % (2 * N)
    end = (end + 2*N - 1) % (2 * N)
    # 내리는 위치에 있는 로봇 내리기
    occupied[-1] = 0
    # 로봇 이동
    for i in range(N-2, -1, -1):
        occupied[i+1] = occupied[i]
    occupied[0] = 0
    occupied[-1] = 0
    # 먼저 올라간 로봇부터 한칸 이동할 수 있다면 이동
    for i in range(N-2, -1, -1):
        if occupied[i] == 0: continue
        idx = (start + i) % (2 * N)
        if arr[(idx + 1) % (2 * N)] and occupied[i+1] == 0:
            occupied[i] = 0
            occupied[i+1] = 1
            arr[(idx + 1) % (2 * N)] -= 1
            if arr[(idx + 1) % (2 * N)] == 0:
                cnt += 1
            if i + 1 == N - 1:
                occupied[i+1] = 0
    # 올리는 칸의 내구도가 0이 아니면 로봇 올리기
    if arr[start]:
        occupied[0] = 1
        arr[start] -= 1
        if arr[start] == 0:
            cnt += 1
    # 내구도 0인 칸의 개수가 K개 이상이면 종료
    if cnt >= K:
        break

print(step)
