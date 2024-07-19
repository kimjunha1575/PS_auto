numbers = []
for i in range(10):
    numbers.append(int(input()))

res = 0
prev = 0
for i in range(10):
    res += numbers[i]
    if res < 100:
        prev = res
        continue
    if res == 100:
        break
    if (100 - prev) >= (res - 100):
        break
    else:
        res = prev
        break

print(res)
