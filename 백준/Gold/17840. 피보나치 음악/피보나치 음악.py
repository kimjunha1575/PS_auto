Q, M = map(int, input().split())
queries = [int(input()) for _ in range(Q)]
visited = dict()
fibonacci = [1, 1]
mod = [1, 1]
period = 0
while True:
    before_prev = fibonacci[period] % M
    prev = fibonacci[period + 1] % M
    if visited.get((before_prev, prev)) is not None:
        break
    fibonacci.append(fibonacci[period] + fibonacci[period + 1])
    mod.append(fibonacci[period + 2] % M)
    visited[(before_prev, prev)] = period
    period += 1
mod.pop()
mod.pop()
target_sequence = []
for e in mod:
    target_sequence += list(str(e))
for query in queries:
    query = (query-1) % len(target_sequence)
    print(target_sequence[query])
