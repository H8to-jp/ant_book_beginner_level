from sys import setrecursionlimit
setrecursionlimit(4100000)
h, w = map(int, input().split())
C = [0 for i in range(h)]
R = [[0 for i in range(w)] for j in range(h)]

def search_dfs(hi:int, wi:int):
    if hi < 0 or h <= hi or wi < 0 or w <= wi or C[hi][wi] == '#' or R[hi][wi] == 1 :
        return 0
    else:
        pass

    R[hi][wi] = 1 

    search_dfs(hi - 1, wi)
    search_dfs(hi + 1, wi)
    search_dfs(hi, wi - 1)
    search_dfs(hi, wi + 1)

    return 0 

for i in range(h):
    C[i] = input()
    for j in range(w):
        if C[i][j] == 's':
            sh, sw = i, j
        elif C[i][j] == 'g':
            gh, gw = i, j
        else:
            pass

search_dfs(sh, sw)

if R[gh][gw] == 1:
    print('Yes')
else:
    print('No')