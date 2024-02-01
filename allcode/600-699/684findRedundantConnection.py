class Solution:
    def findRedundantConnection(self, edges):
        self.d = {}
        for e in edges:
            if e[0] not in self.d:
                self.d[e[0]] = set()
            self.d[e[0]].add(e[1])
            if e[1] not in self.d:
                self.d[e[1]] = set()
            self.d[e[1]].add(e[0])
        m = len(edges)
        for e in range(m-1, -1, -1):
            #print(self.d[edges[e][0]])
            self.d[edges[e][0]].remove(edges[e][1])
            self.d[edges[e][1]].remove(edges[e][0])
            l1 = [edges[e][0]]
            l2 = [edges[e][1]]
            self.findConnectNode(edges[e][0], l1, [])
            if not self.findConnectNode(edges[e][1], l2, l1):
                return edges[e]
            self.d[edges[e][0]].add(edges[e][1])
            self.d[edges[e][1]].add(edges[e][0])

    def findConnectNode(self, p, l1, l2):
        # 查找与p连通的所有点，存在l1中，如果发现存在l2中的点返回失败，否则返回成功
        print(p, l1, l2, self.d[p])
        for i in self.d[p]:
            if i in l2:
                return False
            if i not in l1:
                l1.append(i)
                if not self.findConnectNode(i, l1, l2):
                    return False
        return True


so = Solution()
#print(so.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
#print(so.findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]))
#print(so.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
#print(so.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

class UnionFind:
    def __init__(self, n):
        self.ids = []
        for i in range(n+1):
            self.ids.append(i)
        print(self.ids)
    def union(self, u, v):
        u_id = self.find(u)
        v_id = self.find(v)
        if u_id == v_id:
            return
        for i in range(len(self.ids)):
            if self.ids[i] == u_id:
                self.ids[i] = v_id
    def find(self, p):
        return self.ids[p]
    def connect(self, u, v):
        return self.find(u) == self.find(v)

class Solution1:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges))
        for e in edges:
            print(uf.ids)
            u, v = e[0], e[1]
            if uf.connect(u, v):
                return u, v
            uf.union(u, v)

so = Solution1()
#print(so.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
#print(so.findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]))
#print(so.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
print(so.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))