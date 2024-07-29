N = int(input())
st = []
ans = []
cur_num = 1
for _ in range(N):
    e = int(input())
    if st:
        if e > st[-1]:
            while e >= cur_num:
                st.append(cur_num)
                ans.append('+')
                cur_num += 1
            st.pop()
            ans.append('-')
        elif e == st[-1]:
            st.pop()
            ans.append('-')
        elif e < st[-1]:
            ans = "NO"
            break
    else:
        st.append(cur_num)
        ans.append('+')
        cur_num += 1
        while e >= cur_num:
            st.append(cur_num)
            ans.append('+')
            cur_num += 1
        st.pop()
        ans.append('-')
if ans == "NO":
    print(ans)
else:
    print(*ans, sep='\n')
