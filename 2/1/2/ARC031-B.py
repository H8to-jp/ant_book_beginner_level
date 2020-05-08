from collections import deque
A = [0 for i in range(10)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(10):
    A[i] = input()

def one_island_or_not(M:list):
    t = 0
    R = [[0 for i in range(10)] for j in range(10)]
    for j in range(100):
        hj = j // 10
        wj = j % 10
        if M[hj][wj] == 'o' and R[hj][wj] == 0:
            t += 1
            Q = deque([[hj, wj]])
            if t >= 2:
                return False
            else:
                #DFS
                while len(Q) > 0:
                    for w in range(4):
                        hw = Q[0][0] + D[w][0]
                        ww = Q[0][1] + D[w][1]
                        if 0 <= hw and hw < 10 and 0 <= ww and ww < 10: 
                            if M[hw][ww] == 'o' and R[hw][ww] == 0:
                                R[hw][ww] = 1
                                Q.append([hw, ww])
                            else:
                                R[hw][ww] = 2
                                pass
                        else:
                            pass
                    Q.popleft()
        else:
            pass 
    return True

if one_island_or_not(A) == True:
    print('YES')
else:
    #xのところをひとつづつoに変えていき試してみる
    for i in range(100):
        h = i // 10
        w = i % 10
        if A[h][w] == 'x':
            A[h] = A[h][:w] + 'o' + A[h][w + 1:]
            f = one_island_or_not(A)
            if f == True:
                break
            else:
                pass
            A[h] = A[h][:w] + 'x' + A[h][w + 1:]
    if f == True:
        print('YES')
    else:
        print('NO')