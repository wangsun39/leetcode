# 给你一个无向图，有 n 个节点，编号从 0 到 n - 1。节点 i 的 值 为 nums[i]，可以是 0 或 1。图的边由一个二维数组 edges 给出，其中 edges[i] = [ui, vi] 表示节点 ui 和节点 vi 之间的一条边。
#
# 对于图中节点的 非空子集 s，我们考虑由 s 生成的 诱导子图 如下：
#
# 我们只保留 s 中的节点。
# 我们只保留两个端点都在 s 中的边。
# 返回一个整数，表示图中满足以下条件的节点的 非空 子集 s 的数量：
#
# s 的 诱导子图 是 连通的。
# s 中节点 值 的 总和 是 偶数。
#
#
# 示例 1：
#
# 输入： nums = [1,0,1], edges = [[0,1],[1,2]]
#
# 输出： 2
#
# 解释：
#
# s	是否连通？	节点值总和	和是否为偶数？
# [0]	是	1	否
# [1]	是	0	是
# [2]	是	1	否
# [0,1]	是	1	否
# [0,2]	否，节点 0 和节点 2 不连通。	2	否
# [1,2]	是	1	否
# [0,1,2]	是	2	是
# 示例 2：
#
# 输入： nums = [1], edges = []
#
# 输出： 0
#
# 解释：
#
# s	是否连通？	节点值总和	和是否为偶数？
# [0]	是	1	否
#
#
# 提示：
#
# 1 <= n == nums.length <= 13
# nums[i] 是 0 或 1。
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i] = [ui, vi]
# 0 <= ui < vi < n
# 所有边都是 互不相同 的。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        def check(mask):
            arr = []
            s = 0
            for i in range(n):
                if mask & (1 << i):
                    arr.append(i)
                    s += nums[i]
            if s & 1: return False
            dq = deque([arr[0]])
            s = {arr[0]}
            arr = set(arr)
            while dq:
                x = dq.popleft()
                for y in g[x]:
                    if y in arr and y not in s:
                        s.add(y)
                        dq.append(y)
            return len(s) == len(arr)


        for i in range(1, 1 << n):
            if check(i):
                ans += 1

        return ans


so = Solution()
print(so.evenSumSubgraphs(nums = [1,0,1], edges = [[0,1],[1,2]]))




