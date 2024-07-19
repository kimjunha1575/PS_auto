T = int(input())
for _ in range(T):
    case = input().split()
    cur_max = 0
    move_cnt = 0
    cur_line = []
    for student in range(1, 21):
        new_student = int(case[student])
        new_student_idx = len(cur_line)
        cur_line.append(new_student)
        while new_student_idx > 0 and cur_line[new_student_idx] < cur_line[new_student_idx-1]:
            move_cnt += 1
            tmp = cur_line[new_student_idx]
            cur_line[new_student_idx] = cur_line[new_student_idx-1]
            cur_line[new_student_idx-1] = tmp
            new_student_idx -= 1
    print(f'{int(case[0])} {move_cnt}')
