n, m = map(int, input().split())
D = [[] for i in range(n)]  #Data
for i in range(m):
    ui, vi = map(int, input().split())
    ui, vi = ui - 1, vi - 1
    D[ui].append(vi)
    D[vi].append(ui)
#print("D = ", D)

def dfs_assign_num(t:int, num:int):
    if RD[t] == 0:
        RD[t] = num
        for i in range(len(D[t])):
            dfs_assign_num(D[t][i], num)
    else:
        pass

RD = [0 for i in range(n)]   #Record for DFS
gnum = 0
for i in range(n):
    if RD[i] == 0:
        gnum += 1
        dfs_assign_num(i, gnum)
    else:
        pass
#print("RD = ", RD)

CPB = [[0, 0] for i in range(gnum)]   #Count Point and Branch
for i in range(n):
    CPB[RD[i] - 1][0] += 1
    CPB[RD[i] - 1][1] += len(D[i])
#print("CPB", CPB)

ans = 0
for i in range(gnum):
    pi = CPB[i][0]      #point num _i
    bi = CPB[i][1] // 2 #branch num _i
    if pi - 1 == bi:
        ans += 1
    else:
        pass
print(ans)