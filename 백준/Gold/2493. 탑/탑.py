N = int(input())
arr = list(map(int, input().split()))
st = []
ans = []
for i in range(N):
    cur = arr[i]
    if st:
        prev = st[-1]
        if prev[0] > cur:
            st.append((cur, i+1))
            ans.append(prev[1])
        else:
            while st and st[-1][0] <= cur:
                prev = st.pop()
            if st:
                prev = st[-1]
                st.append((cur, i+1))
                ans.append(prev[1])
            else:
                st.append((cur, i+1))
                ans.append(0)
    else:
        st.append((cur, i+1))
        ans.append(0)
print(*ans, sep=' ')
