string = input()
high = "*/"
low = "+-"
st = []
for e in string:
    if e == '(':
        st.append(e)
    elif e == ')':
        while st[-1] != '(':
            print(st.pop(), end='')
        st.pop()
    elif e in high:
        while st and st[-1] != '(' and (st[-1] in high):
            print(st.pop(), end='')
        st.append(e)
    elif e in low:
        while st and st[-1] != '(':
            print(st.pop(), end='')
        st.append(e)
    else:
        print(e, end='')
while st:
    print(st.pop(), end='')
