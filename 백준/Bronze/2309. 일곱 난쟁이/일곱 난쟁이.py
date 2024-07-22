def prt(arr, i, j):
    for idx in range(len(arr)):
        if idx == i or idx == j:
            continue
        print(arr[idx])


li = []
for _ in range(9):
    li.append(int(input()))
li.sort()
total = sum(li)
target = total - 100
flag = False
for i in range(0, 8):
    if flag:
        break
    for j in range(i+1, 9):
        if li[i] + li[j] == target:
            flag = True
            prt(li, i, j)
            break
