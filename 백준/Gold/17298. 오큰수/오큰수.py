N = int(input())
arr = list(map(int, input().split()))
st = []
ans = []
while arr:
    num = arr.pop()
    if st:
        prev = st[-1]
        st.append(num)
        if num < prev:
            ans.append(prev)
        else:
            while st and st[-1] <= num:
                tmp = st.pop()
            if st:
                prev = st[-1]
                st.append(num)
                ans.append(prev)
            else:
                st.append(num)
                ans.append(-1)
    else:
        st.append(num)
        ans.append(-1)

print(*ans[-1::-1], sep=' ')
