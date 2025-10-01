def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5 + 1)):
        if (x % i == 0):
            return False
    return True

def solution(n, k):
    answer = 0
    num = 0
    while n > 0:
        acc = 1
        tmp = 1
        while (n >= tmp * k):
            tmp *= k
            acc *= 10
        n -= tmp
        num += acc
    tmp = str(num)
    candidates = tmp.replace('0', ' ').split()
    for cand in candidates:
        if isPrime(int(cand)):
            answer += 1
    return answer
