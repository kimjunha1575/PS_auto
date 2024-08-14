'''
절단기에 설정할 높이를 이진탐색으로 찾는다고 했을 때
높이 x에 대해 상근이가 가져갈 수 있는 나무의 총 길이를 구하는 과정이 O(N)
높이 x를 찾는 과정이 O(log(N))
따라서 O(N*log(N))으로 해결 가능하고

나무의 총 개수가 최대 100만개
나무의 최대 높이가 20억

따라서 최대 100만 * log(20억) 번의 연산 필요
러프하게 잡아도 5천만번 안에 해결 가능
'''



def calc_yield(height):
    res = 0
    for tree in trees:
        if tree > height:
            res += tree - height
    if res >= M:
        return True
    return False


def binary_search():
    left = 0
    right = trees[-1]
    while left <= right:
        mid = (left + right) // 2
        if calc_yield(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
print(binary_search())
