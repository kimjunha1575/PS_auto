'''
1515 문제 읽고 구상 1
1520 구현
1526 오픈된 테케에 대해 정답 확인, 제출


구상 1
문제 조건 상 거북이가 지나가는 모든 좌표에 대해
(최소행, 최소열) ~ (최대행, 최대열)로 만들어지는 직사각형이 최대일 것이라고 생각
거북이의 방향과 위치좌표를 트래킹하면서 행, 열값의 최소, 최대를 갱신하고
그에 따라 만들어지는 직사각형의 넓이를 출력한다.
갱신하는 구조이므로 초기값 설정에 주의하고
이동한 영역이 선분일 경우 자연스럽게 결과가 0이 나오도록 설계하면 깔끔해질 것.


'''

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())
for case in range(T):
    program = input()
    tur_y = 0
    tur_x = 0
    tur_dir = 3 # directions[3]
    max_y, max_x, min_y, min_x = 0, 0, 0, 0
    for command in program:
        if command == 'F':
            tur_y += directions[tur_dir][0]
            tur_x += directions[tur_dir][1]
        elif command == 'B':
            tur_y -= directions[tur_dir][0]
            tur_x -= directions[tur_dir][1]
        elif command == 'R':
            tur_dir = (tur_dir + 1) % 4
        else:
            tur_dir = (tur_dir - 1) % 4
        max_y = max(max_y, tur_y)
        max_x = max(max_x, tur_x)
        min_y = min(min_y, tur_y)
        min_x = min(min_x, tur_x)
    print((max_y - min_y) * (max_x - min_x))
