S = input()
n = 4

for i in range(2 ** (n - 1)):
    r = int(S[0])
    for j in range(n - 1):
        if (i >> j) & 1 == 1:
            r -= int(S[j + 1])
        else:
            r += int(S[j + 1])
    if r == 7:
        p = i
        break
    else:
        pass

for i in range(n - 1):
    print(S[i], end = '')
    if (p >> i) & 1 == 1:
        print('-', end = '')
    else:
        print('+', end = '')
print(S[3], end = '') 
print('=7')