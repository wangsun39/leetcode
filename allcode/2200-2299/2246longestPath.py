# 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
#
# 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
#
# 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。
#
#
#
# 示例 1：
#
#
#
# 输入：parent = [-1,0,0,1,1,2], s = "abacbe"
# 输出：3
# 解释：任意一对相邻节点字符都不同的最长路径是：0 -> 1 -> 3 。该路径的长度是 3 ，所以返回 3 。
# 可以证明不存在满足上述条件且比 3 更长的路径。
# 示例 2：
#
#
#
# 输入：parent = [-1,0,0,0], s = "aabc"
# 输出：3
# 解释：任意一对相邻节点字符都不同的最长路径是：2 -> 0 -> 3 。该路径的长度为 3 ，所以返回 3 。
#
#
# 提示：
#
# n == parent.length == s.length
# 1 <= n <= 105
# 对所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
# parent[0] == -1
# parent 表示一棵有效的树
# s 仅由小写英文字母组成




from leetcode.allcode.competition.mypackage import *
class Solution:

    def longestPath1(self, parent: List[int], s: str) -> int:
        N = len(parent)
        son = [[] for _ in range(N)]
        for idx, p in enumerate(parent):
            if p == -1:
                continue
            if len(son[p]) != 0:
                son[p].append(idx)
            else:
                son[p] = [idx]
        val = [''] * N
        for i in range(N):
            val[i] = s[i]
        print(son)

        @lru_cache(None)
        def find(parent, kid):
            if val[parent] != val[kid]:
                maxL = 2
                for e in son[kid]:
                    length = find(kid, e)
                    maxL = max(length + 1, maxL)
                return maxL
            else:
                return 1
        def findFrom(parent):
            maxL = []
            if len(son[parent]) == 0:
                return 1
            for e in son[parent]:
                maxL.append(find(parent, e))
            if len(maxL) == 1:
                return maxL[0]
            maxL.sort()
            return maxL[-1] + maxL[-2] - 1
        maxL = 0
        for i in range(N):
            maxL = max(maxL, findFrom(i))
        return maxL

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p == -1: continue
            graph[i].append(p)
            graph[p].append(i)
        ans = 1
        def dfs(x, fa):
            nonlocal ans
            mx = 0
            for y in graph[x]:
                if y == fa: continue
                if s[y] == s[x]:
                    dfs(y, x)
                    continue
                mx_sub = dfs(y, x)
                ans = max(ans, mx + mx_sub + 1)
                mx = max(mx, mx_sub)
            return mx + 1
        dfs(0, -1)
        return ans


so = Solution()
print(so.longestPath(parent = [-1,0,1], s = "aab"))
print(so.longestPath(parent = [-1,0,0,0], s = "aabc"))
print(so.longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))


