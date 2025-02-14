# 给你一个整数n，表示一张无向图中有 n个节点，编号为0到n - 1。同时给你一个二维整数数组edges，其中edges[i] = [ai, bi]表示节点ai 和bi之间有一条无向边。
#
# 请你返回 无法互相到达的不同 点对数目。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, edges = [[0,1],[0,2],[1,2]]
# 输出：0
# 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
# 示例 2：
#
#
#
# 输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# 输出：14
# 解释：总共有 14 个点对互相无法到达：
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
# 所以我们返回 14 。
#
#
# 提示：
#
# 1 <= n <= 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# 不会有重复边。

from leetcode.allcode.competition.mypackage import *

# bit位 函数：
# n.bit_length()
# value = int(s, 2)
class UnionFind:
    def __init__(self, n):
        self.ids = []
        for i in range(n):
            self.ids.append(i)
    def union(self, u, v):
        u_id = self.find(u)
        # v_id = self.find(v)
        # if v == u_id:
        #     return False
        self.ids[v] = u_id
        # for i in range(len(self.ids)):
        #     if self.ids[i] == v:
        #         self.ids[i] = u_id
    def find(self, p):
        if p == self.ids[p]:
            return p
        self.ids[p] = self.find(self.ids[p])
        return self.ids[p]
class Solution:
    #
    def countPairs1(self, n: int, edges: List[List[int]]) -> int:
        flag = [False] * n  # 表示是否计算过
        graph = defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        def dfs(idx):
            nonlocal size
            flag[idx] = True
            size += 1
            for j in graph[idx]:
                if not flag[j]:
                    dfs(j)
        ans = 0
        for i in range(n):
            if flag[i]:
                continue
            size = 0
            dfs(i)
            ans += (size * (n - size))
        return ans // 2

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 2023/10/21 并查集
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for x, y in edges:
            union(x, y)
        d = defaultdict(int)
        for i in range(n):
            x = find(i)
            d[x] += 1
        ans = 0
        for v in d.values():
            ans += v * (n - v)
        return ans // 2



d= {0: 0, 3: 0, 22: 0, 65: 0, 1: 1, 9: 1, 45: 1, 2: 2, 14: 2, 57: 2, 12: 0, 23: 0, 26: 0, 27: 0, 64: 0, 4: 4, 37: 4, 44: 4, 46: 16, 5: 4, 6: 6, 15: 6, 7: 1, 8: 8, 10: 8, 13: 8, 19: 8, 18: 1, 30: 1, 32: 1, 33: 1, 62: 1, 38: 8, 11: 11, 28: 11, 35: 11, 50: 11, 17: 0, 61: 0, 72: 0, 36: 8, 40: 2, 48: 2, 25: 6, 16: 16, 24: 16, 42: 16, 20: 8, 31: 8, 21: 11, 70: 11, 43: 16, 29: 6, 34: 6, 41: 0, 73: 0, 76: 0, 75: 0, 47: 8, 52: 8, 56: 1, 68: 1, 78: 1, 54: 11, 66: 11, 71: 11, 53: 8, 60: 8, 39: 1, 49: 2, 69: 16, 58: 8, 55: 2, 81: 2, 51: 2, 67: 11, 74: 11, 79: 2, 59: 11, 83: 11, 63: 2, 84: 2, 77: 0, 80: 1, 82: 0}

dd = defaultdict(set)
for i in d:
    dd[d[i]].add(i)


so = Solution()
print(so.countPairs(85, [[65,0],[1,45],[57,2],[3,0],[46,4],[46,5],[46,6],[7,45],[1,9],[10,8],[50,11],[12,3],[8,13],[14,2],[6,15],[46,16],[17,12],[18,9],[19,8],[20,19],[50,21],[22,0],[3,23],[24,16],[15,25],[3,26],[27,3],[11,28],[29,25],[30,9],[20,31],[32,9],[33,9],[34,25],[11,35],[36,13],[37,4],[10,38],[45,39],[40,14],[26,41],[42,16],[43,24],[4,44],[31,47],[48,14],[49,40],[49,51],[52,31],[36,53],[54,35],[48,55],[56,33],[47,58],[59,54],[60,38],[12,61],[62,9],[57,63],[64,3],[35,66],[50,67],[33,68],[46,69],[70,21],[35,71],[12,72],[26,73],[50,74],[75,27],[26,76],[77,64],[33,78],[51,79],[80,68],[48,81],[82,75],[54,83],[63,84]]))  # 0
print(so.countPairs(16, [[0,15],[1,14],[2,11],[4,3],[5,15],[8,2],[14,12]]))  # 0
print(so.countPairs(n = 11, edges = [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]))  # 0
print(so.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))  # 14
print(so.countPairs(5, [[1,0],[3,1],[0,4],[2,1]]))  # 0
print(so.countPairs(20, [[0,1],[0,2],[3,0],[4,0],[0,5],[6,0],[0,7],[0,8],[9,0],[10,0],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[18,0],[0,19],[2,1],[3,1],[4,1],[1,5],[1,6],[1,7],[8,1],[9,1],[1,10],[1,11],[12,1],[13,1],[14,1],[15,1],[16,1],[17,1],[1,18],[19,1],[2,3],[4,2],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[12,2],[13,2],[14,2],[15,2],[16,2],[17,2],[2,18],[2,19],[3,4],[3,5],[3,6],[7,3],[8,3],[3,9],[3,10],[3,11],[3,12],[13,3],[14,3],[15,3],[16,3],[17,3],[3,18],[3,19],[5,4],[4,6],[7,4],[8,4],[4,9],[10,4],[4,11],[4,12],[4,13],[14,4],[4,15],[4,16],[4,17],[18,4],[19,4],[5,6],[7,5],[8,5],[9,5],[5,10],[5,11],[12,5],[5,13],[5,14],[15,5],[16,5],[17,5],[5,18],[19,5],[7,6],[6,8],[6,9],[10,6],[11,6],[6,12],[13,6],[6,14],[15,6],[6,16],[17,6],[18,6],[19,6],[7,8],[9,7],[10,7],[11,7],[7,12],[7,13],[14,7],[15,7],[7,16],[7,17],[18,7],[19,7],[8,9],[10,8],[11,8],[8,12],[8,13],[8,14],[15,8],[8,16],[17,8],[18,8],[8,19],[9,10],[9,11],[12,9],[9,13],[14,9],[15,9],[9,16],[9,17],[9,18],[9,19],[10,11],[12,10],[13,10],[14,10],[10,15],[16,10],[17,10],[10,18],[19,10],[12,11],[13,11],[11,14],[15,11],[11,16],[11,17],[18,11],[11,19],[12,13],[12,14],[12,15],[12,16],[12,17],[18,12],[12,19],[14,13],[15,13],[16,13],[17,13],[13,18],[13,19],[15,14],[14,16],[14,17],[14,18],[14,19],[15,16],[17,15],[15,18],[15,19],[16,17],[16,18],[16,19],[18,17],[19,17],[18,19]]))

print(so.countPairs(n = 3, edges = [[0,1],[0,2],[1,2]]))  # 0




