def tiktok(gender, number):
    # 남학생
    if gender == 1:
        for i in range(0, N):
            if (i + 1) % number == 0:
                switches[i] = 1 - switches[i]
    # 여학생
    else:
        number -= 1
        switches[number] = 1 - switches[number]
        idx = 1
        while number + idx < N and number - idx >= 0\
            and switches[number + idx] == switches[number - idx]:
            switches[number + idx] = 1 - switches[number + idx]
            switches[number - idx] = 1 - switches[number - idx]
            idx += 1


N = int(input())
switches = list(map(int, input().split()))
query_num = int(input())
queries = [tuple(map(int, input().split())) for _ in range(query_num)]
for query in queries:
    tiktok(*query)

stk = 0
for switch in switches:
    print(switch, end=' ')
    stk += 1
    if stk == 20:
        print()
        stk = 0
