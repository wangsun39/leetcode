# 给你一个 n个节点的 有向图，节点编号为0到n - 1，其中每个节点至多有一条出边。
#
# 图用一个大小为 n下标从0开始的数组edges表示，节点 i到节点edges[i]之间有一条有向边。如果节点i没有出边，那么edges[i] == -1。
#
# 请你返回图中的 最长环，如果没有任何环，请返回 -1。
#
# 一个环指的是起点和终点是 同一个节点的路径。
#
#
#
# 示例 1：
#
#
#
# 输入：edges = [3,3,4,2,3]
# 输出去：3
# 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
# 这个环的长度为 3 ，所以返回 3 。
# 示例 2：
#
#
#
# 输入：edges = [2,-1,3,1]
# 输出：-1
# 解释：图中没有任何环。
#
#
# 提示：
#
# n == edges.length
# 2 <= n <= 105
# -1 <= edges[i] < n
# edges[i] != i


from leetcode.allcode.competition.mypackage import *
class Solution:
    def longestCycle1(self, edges: List[int]) -> int:
        # @lru_cache(None)
        n = len(edges)
        flag = [0] * n
        ans = -1
        def dfs(node):
            nonlocal ans
            if flag[node]:
                return
            d = {}
            dis = 0
            while 0 == flag[node] and -1 != edges[node]:
                d[node] = dis
                dis += 1
                flag[node] = 1
                node = edges[node]
            if -1 == edges[node]:
                return
            if node in d:
                ans = max(ans, dis - d[node])
        for i in range(n):
            dfs(i)
        return ans
    def longestCycle(self, edges: List[int]) -> int:
        # 拓扑排序实现 2023/1/18
        # 这题还是 DFS 更容易实现
        def buildTopo(conditions, n):  # 迭代删除入度为 1 的点
            tree = defaultdict(set)
            pre_num = [0] * n
            for x, y in enumerate(conditions):
                if y != -1 and y not in tree[x]:
                    tree[x].add(y)
                    pre_num[y] += 1
            queue = deque([i for i in range(n) if pre_num[i] == 0])
            ans = set([i for i in range(n)])
            while len(queue):
                q = queue.popleft()
                ans.remove(q)
                for x in tree[q]:
                    pre_num[x] -= 1
                    if pre_num[x] == 0:
                        queue.append(x)
            return list(ans)
        n = len(edges)
        # start = time.time_ns()
        remain = buildTopo(edges, n)
        # print((time.time_ns() - start) / (1000 * 1000))
        # if len(remain) == 0: return -1
        flag = {k: 0 for k in remain}
        ans = -1
        for x in remain:
            if flag[x] > 0: continue
            length = 0
            while flag[x] == 0:
                flag[x] = 1
                length += 1
                x = edges[x]
            ans = max(ans, length)
        # print((time.time_ns() - start) / (1000 * 1000))
        return ans

    def longestCycle(self, edges: List[int]) -> int:
        def buildTopo(conditions, n):
            pre = set(i for i in range(n))
            for x, y in enumerate(conditions):
                if y != -1:
                    pre[y].add(x)
            return [pre[x] for x in pre]


        n = len(edges)
        left = buildTopo(edges, n)

        if len(left) == 0: return -1
        ans = 0
        while len(left):
            x = left[0]
            left.remove(x)
            length = 0
            while True:
                y = edges[x]
                length += 1
                if y not in left: break
                left.remove(y)
                x = y
            ans = max(ans, length)
        return ans




so = Solution()
print(so.longestCycle([3,3,4,2,3]))
print(so.longestCycle([2,-1,3,1]))




