def solve(exp):
    if exp == 1:
        return R
    k = solve(exp//2)
    if exp % 2:
        return (k * k * A) % C
    else:
        return (k * k) % C


A, B, C = map(int, input().split())
R = A % C
print(solve(B))
