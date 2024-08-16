'''

이전 [11053 가장 긴 증가하는 부분 수열] 문제에서
각 원소마다 첫 원소부터 해당 원소 이전 원소까지를 순회하면서
가장 긴 수열의 길이를 갱신하는 구조
O(N^2)의 시간복잡도를 가진다. (j번째 원소에서 0번째부터 j-1번째 원소까지 확인)

아래 풀이는 같은 문제를 O(N*log(N))의 시간복잡도로 해결할 수 있는 풀이임

                   *** 핵심 포인트 ***
1. 0번째부터 마지막 원소까지 순회하는 구조는 기존과 동일
2. 현재 원소까지의 가장 긴 증가하는 부분 수열의 길이를 트래킹하기 위한 dp 배열 사용
3. (중요) dp 배열은 현재까지의 가장 긴 증가하는 부분 수열과 같지 않다
4. 원래 수열의 모든 원소에 대해 순서대로 5와 6을 반복한다
5. dp 배열의 뒤로 추가될 수 있는 원소를 만나면 추가한다
6. dp 배열의 뒤로 추가할 수 없는 원소(배열의 마지막 원소보다 작거나 같은 원소)를 만나면
   dp 배열의 원소 중 해당 원소보다 크거나 같은 첫 원소를 해당 원소로 교체한다
   (이 때 dp 배열은 정렬되어 있으므로 이진탐색으로 찾을 수 있다. 그래서 O(N * log(N)))

'''


def find_idx(target):
    # target보다 크거나 같은 첫 원소의 인덱스를 반환
    left = 0
    right = len(dp) - 1
    while left <= right:
        mid = (left + right) // 2
        if target <= dp[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


N = int(input())
arr = list(map(int, input().split()))
dp = []
for i in range(N):
    if not dp:
        # dp 배열이 비어 있다면 그냥 추가
        dp.append(arr[i])
    elif arr[i] > dp[-1]:
        # dp 배열의 뒤로 추가할 수 있다면 뒤로 추가
        dp.append(arr[i])
    else:
        # 나머지 경우에 대해선 해당 원소가 들어갈 자리를 찾아서 교체
        idx = find_idx(arr[i])
        dp[idx] = arr[i]
# dp 배열의 길이가 곧 LIS의 길이
print(len(dp))
