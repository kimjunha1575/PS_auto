def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    left_idx = 0
    right_idx = 0
    res = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    res.extend(left[left_idx:])
    res.extend(right[right_idx:])
    return res


N = int(input())
ori = [int(input()) for _ in range(N)]
ans = merge_sort(ori)
for e in ans:
    print(e)
