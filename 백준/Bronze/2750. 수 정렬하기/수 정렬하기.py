def my_sort(arr, left, right):
    if right < left:
        return
    pivot = right
    right -= 1
    while left <= right:
        if arr[right] >= arr[pivot]:
            right -= 1
            continue
        if arr[left] <= arr[pivot]:
            left += 1
            continue
        if arr[right] < arr[pivot] < arr[left]:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1
    arr[pivot], arr[left] = arr[left], arr[pivot]
    my_sort(arr, 0, right)
    my_sort(arr, left + 1, pivot)


N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

my_sort(li, 0, len(li) - 1)
for e in li:
    print(e)
