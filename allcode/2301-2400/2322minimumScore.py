# 存在一棵无向连通树，树中有编号从 0 到 n - 1 的 n 个节点， 以及 n - 1 条边。
#
# 给你一个下标从 0 开始的整数数组 nums ，长度为 n ，其中 nums[i] 表示第 i 个节点的值。另给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边。
#
# 删除树中两条 不同 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：
#
# 分别获取三个组件 每个 组件中所有节点值的异或值。
# 最大 异或值和 最小 异或值的 差值 就是这一种删除边方案的分数。
# 例如，三个组件的节点值分别是：[4,5,7]、[1,9] 和 [3,3,3] 。三个异或值分别是 4 ^ 5 ^ 7 = 6、1 ^ 9 = 8 和 3 ^ 3 ^ 3 = 3 。最大异或值是 8 ，最小异或值是 3 ，分数是 8 - 3 = 5 。
# 返回在给定树上执行任意删除边方案可能的 最小 分数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
# 输出：9
# 解释：上图展示了一种删除边方案。
# - 第 1 个组件的节点是 [1,3,4] ，值是 [5,4,11] 。异或值是 5 ^ 4 ^ 11 = 10 。
# - 第 2 个组件的节点是 [0] ，值是 [1] 。异或值是 1 = 1 。
# - 第 3 个组件的节点是 [2] ，值是 [5] 。异或值是 5 = 5 。
# 分数是最大异或值和最小异或值的差值，10 - 1 = 9 。
# 可以证明不存在分数比 9 小的删除边方案。
# 示例 2：
#
#
# 输入：nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
# 输出：0
# 解释：上图展示了一种删除边方案。
# - 第 1 个组件的节点是 [3,4] ，值是 [4,4] 。异或值是 4 ^ 4 = 0 。
# - 第 2 个组件的节点是 [1,0] ，值是 [5,5] 。异或值是 5 ^ 5 = 0 。
# - 第 3 个组件的节点是 [2,5] ，值是 [2,2] 。异或值是 2 ^ 2 = 0 。
# 分数是最大异或值和最小异或值的差值，0 - 0 = 0 。
# 无法获得比 0 更小的分数 0 。
#
#
# 提示：
#
# n == nums.length
# 3 <= n <= 1000
# 1 <= nums[i] <= 108
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵有效的树

from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ins = [0] * n  # 记录每个节点进入的时间
        outs = [0] * n  # 记录每个节点出来的时间
        xors = [0] * n  # 以x为根节点的子树的异或值
        Fa = [0] * n
        t = 0  # 记录时间
        s = reduce(lambda x, y: x ^ y, nums)  # 总的异或和

        def dfs(x, fa):
            nonlocal t
            Fa[x] = fa
            ins[x] = t
            t += 1
            res = nums[x]
            for y in g[x]:
                if y != fa:
                    res ^= dfs(y, x)
            outs[x] = t
            xors[x] = res
            t += 1
            return res

        dfs(0, -1)
        ans = inf
        for i in range(n - 1):
            x, y = edges[i]
            if Fa[x] == y:
                x, y = y, x
            # 保证x是y的父节点
            for j in range(i + 1, n - 1):
                u, v = edges[j]
                if Fa[u] == v:
                    u, v = v, u
                if ins[y] <= ins[u] <= outs[y]:
                    # u在y的子树上
                    a = s ^ xors[y]
                    b = xors[v]
                    c = s ^ a ^ b
                    ans = min(ans, max(a, b, c) - min(a, b, c))
                elif ins[v] <= ins[x] <= outs[v]:
                    # x在v的子树上
                    a = s ^ xors[v]
                    b = xors[y]
                    c = s ^ a ^ b
                    ans = min(ans, max(a, b, c) - min(a, b, c))
                else:
                    # x, y 在两个子树上
                    a = xors[y]
                    b = xors[v]
                    c = s ^ a ^ b
                    ans = min(ans, max(a, b, c) - min(a, b, c))
        return ans

so = Solution()
print(so.minimumScore(nums = [28,24,29,16,31,31,17,18], edges = [[0,1],[6,0],[6,5],[6,7],[3,0],[2,1],[2,4]]))
print(so.minimumScore(nums = [29,29,23,32,17], edges = [[3,1],[2,3],[4,1],[0,4]]))
print(so.minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))




