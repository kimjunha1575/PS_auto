'''
그냥 123부터 987까지의 모든 순열에 대해 검사함
각 자리가 같으면 스트라이크에서 1을 빼고
다르지만 사용된 숫자라면 볼에서 1을 빼서
스트라이크와 볼이 둘 다 0이라면 정답에 1을 더함
'''


def is_possible(arr):
    for query in queries:
        # 모든 문답에 대해
        num = list(map(int, str(query[0])))
        strike = query[1]
        ball = query[2]
        for x, y in zip(num, arr):
            # 일치한다면 스트라이크 - 1
            if y == x:
                strike -= 1
            # 자리는 다르지만 사용한 숫자라면 볼 -1
            elif y in num:
                ball -= 1
        # 하나라도 0이 아니라면 즉시 종료
        if strike or ball:
            return False
    # 모든 문답에 대해 결과가 일치한다면 True 반환
    return True


def solve(idx):
    if idx == 3:
        if is_possible(buf):
            # 모든 문답에 대해 결과가 일치한다면 정답 + 1
            global ans
            ans += 1
        return
    for i in range(1, 10):
        # 1 ~ 9까지 중복 없이 세 자리를 뽑는 순열
        if used[i]: continue
        used[i] = 1
        buf.append(i)
        solve(idx + 1)
        buf.pop()
        used[i] = 0


N = int(input())
queries = [tuple(map(int, input().split())) for _ in range(N)]
buf = []
used = [0] * 10
ans = 0
solve(0)
print(ans)
