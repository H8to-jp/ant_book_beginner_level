from itertools import product
S = input()

n = len(S)
ans = 0
for P in product([0, 1], repeat= n - 1):
    b = 0   #before
    tmp = 0
    for i in range(len(P)):
        if P[i] == 1:
            tmp += int(S[b:i + 1])
            b = i + 1
        else:
            pass
    tmp += int(S[b:n])
    ans += tmp
print(ans)