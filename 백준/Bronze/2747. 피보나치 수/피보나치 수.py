def solve(n):
    if fibonacci[n]: return fibonacci[n]
    fibonacci[n] = solve(n-1) + solve(n-2)
    return fibonacci[n]


N = int(input())
fibonacci = [0, 1, 1] + [0] * N
print(solve(N))
