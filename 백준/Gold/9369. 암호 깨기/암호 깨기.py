

T = int(input())
for case in range(T):
    N = int(input())
    encrypted = [input() for _ in range(N)]
    decrypted = input()
    target = input()
    valid_tables = []
    for e in encrypted:
        if len(e) != len(decrypted): continue
        valid = True
        decrypt_table = [0] * 26
        used = [0] * 26
        for i in range(len(e)):
            en_idx = ord(e[i]) - ord('a')
            de_idx = ord(decrypted[i]) - ord('a')
            # 이미 정해진 문자라면 다음으로
            if decrypt_table[en_idx] == decrypted[i]: continue
            # 다른 문자와 연결되는 경우 무효
            if decrypt_table[en_idx] != 0:
                valid = False
                break
            # 정해진 문자가 아닌데 이미 사용한 문자로 연결된다면 무효
            if used[de_idx]:
                valid = False
                break
            decrypt_table[en_idx] = decrypted[i]
            used[de_idx] = 1
        if valid and sum(used) == 25:
            for i in range(26):
                if used[i] == 0:
                    unused_char = chr(i + ord('a'))
                    break
            for i in range(26):
                if decrypt_table[i] == 0:
                    decrypt_table[i] = unused_char
                    break
        if valid:
            valid_tables.append(decrypt_table)
    if valid_tables:
        ans = ''
        for c in target:
            valid = True
            idx = ord(c) - ord('a')
            encrypted_char = valid_tables[0][idx]
            for i in range(1, len(valid_tables)):
                if encrypted_char != valid_tables[i][idx]:
                    valid = False
                    break
            if valid and encrypted_char != 0:
                ans += encrypted_char
            else:
                ans += '?'
        print(ans)
    else:
        print("IMPOSSIBLE")


