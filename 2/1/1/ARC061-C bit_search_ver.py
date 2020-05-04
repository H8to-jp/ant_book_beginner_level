S = input()

n = len(S) - 1
ans = 0
for i in range(2 ** n):
    b = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            ans += int(S[b:j + 1])
            b = j + 1
        else:
            pass
    ans += int(S[b:])
print(ans)