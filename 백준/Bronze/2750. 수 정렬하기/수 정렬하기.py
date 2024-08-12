# left 배열과 right 배열을 받아서 정렬된 하나의 배열로 만들어 반환
def merge(left, right):
    left_idx = 0
    right_idx = 0
    res = []
    # 인덱스를 넘겨가면서 더 작은 원소를 하나씩 res에 추가
    # 한쪽 배열이 전부 추가될 때 까지 반복
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    # 둘 중 하나의 배열에 원소가 남아 있으므로 남은 배열을 res 배열의 뒤에 추가
    res.extend(left[left_idx:])
    res.extend(right[right_idx:])
    return res


def merge_sort(arr):
    # 배열의 길이가 1 이하라면 그대로 반환
    if len(arr) <= 1:
        return arr
    # 배열을 반으로 나누고
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 순서대로 정렬해서 합친 배열을 반환
    return merge(left, right)


N = int(input())
ori = [int(input()) for _ in range(N)]
ans = merge_sort(ori)
for e in ans:
    print(e)
