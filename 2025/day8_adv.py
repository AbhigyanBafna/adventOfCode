import math


with open("input.txt", "r") as file:
    jbs = [(list(map(int, line.strip().split(',')))) for line in file]

n = len(jbs)

dist = []
for i in range(n):
    x1,y1,z1 = jbs[i]
    for j in range(i+1,n):
        x2,y2,z2 = jbs[j]
        euc = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )
        dist.append((euc, i, j))

dist.sort(key=lambda euc: euc[0])


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(0,n)]
        return


    def find(self, x):
        t = self.parent[x]
        while self.parent[t] != t:
            t = self.parent[t]

        self.parent[x] = t #Path Compression
        return t


    def union(self,x,y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            self.parent[a] = b
            return 0
        return 1


uf = UnionFind(n)

ans = 0

for item in dist:
    jb1 = item[1]
    jb2 = item[2]

    diff = uf.union(jb1,jb2)
    
    if diff == 0:
        jb1_x, jb2_x = jbs[jb1][0], jbs[jb2][0]
        ans = jb1_x * jb2_x
        

print(ans)