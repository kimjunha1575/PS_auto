'''
현재 정사각형에서 4개로 나누었을 때 어디에 속하는 지 찾는다
0 1
2 3

i번째라면 i * 2**(n-1) * 2**(n-1) 을 더한다
n이 0일 때 기저
'''


def find_quad_pos(n, r, c):
    global ans
    if n == 0:
        ans += 2*r + c
        return
    l = 2 ** (n-1)
    one_portion = l**2
    if r + 1 > l and c + 1 > l:
        ans += 3 * one_portion
        find_quad_pos(n-1, r - l, c - l)
    elif r + 1 > l:
        ans += 2 * one_portion
        find_quad_pos(n-1, r - l, c)
    elif c + 1 > l:
        ans += 1 * one_portion
        find_quad_pos(n-1, r, c - l)
    else:
        find_quad_pos(n-1, r, c)


N, r, c = map(int, input().split())
ans = 0
find_quad_pos(N, r, c)
print(ans)
