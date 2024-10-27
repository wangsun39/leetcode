# 树可以看成是一个连通且 无环 的 无向 图。
#
# 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
#
# 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的那个。
#
#
#
# 示例 1：
#
#
#
# 输入: edges = [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 示例 2：
#
#
#
# 输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
#
#
# 提示:
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# edges 中无重复元素
# 给定的图是连通的

from leetcode.allcode.competition.mypackage import *

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
    def findRedundantConnection1(self, edges):
        uf = UnionFind(len(edges))
        for e in edges:
            print(uf.ids)
            u, v = e[0], e[1]
            if uf.connect(u, v):
                return u, v
            uf.union(u, v)

    def findRedundantConnection(self, edges):
        g = defaultdict(list)
        n = len(edges)
        deg = [0] * (n + 1)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1
        dq = deque([i for i in range(n + 1) if deg[i] == 1])
        left = set(range(1, n + 1))  # 剩余的点
        for x in dq:
            left.remove(x)
            deg[x] = 0
        while dq:  # 不断删除度为1的点
            x = dq.popleft()
            for y in g[x]:
                if y not in left: continue
                deg[y] -= 1
                if deg[y] == 1:
                    dq.append(y)
                    left.remove(y)
        for x, y in edges[::-1]:
            if x in left and y in left:
                return [x, y]



so = Solution1()
#print(so.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
#print(so.findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]))
#print(so.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
print(so.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))