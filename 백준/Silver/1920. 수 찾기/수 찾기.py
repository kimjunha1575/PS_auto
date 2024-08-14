def binary_search(target):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # 찾으면 1 반환
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # 못 찾으면 0 반환
    return 0


N = int(input())
arr = list(map(int, input().split()))
# 이진탐색을 위해 미리 정렬
arr.sort()
Q = int(input())
queries = list(map(int, input().split()))
for query in queries:
    print(binary_search(query))
