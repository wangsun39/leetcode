# 给你一棵有 n 个节点的有根树，节点编号从 0 到 n - 1 ，由一个长度为 n 的整数数组 parent 表示，其中：
#
# parent[0] = -1 （节点 0 是根节点）。
# 对于每个 1 <= i < n ，parent[i] 是节点 i 的父节点（0 <= parent[i] < i）。
# 另外给你一个长度为 n 的整数数组 nums ，其中 nums[i] 是节点 i 的值，以及一个整数 k。
#
# 如果节点的一个非空子集满足以下条件，则称为 有效 子集：
#
# 所选节点的值之 和 可以被 k 整除 。
# 所选节点中没有 两 个节点在树中是 相邻 的（即没有节点及其直接父节点同时包含在子集中）。
# 返回有效子集的数量对 109 + 7 取余的结果。
#
#
#
# 示例 1：
#
# 输入： parent = [-1,0,1], nums = [1,2,3], k = 3
#
# 输出： 1
#
# 解释：
#
#
#
# 唯一有效的子集是 {2} 。它包含值为 3 的节点 2，可以被 3 整除。
#
# 示例 2：
#
# 输入： parent = [-1,0,0,0], nums = [2,1,2,1], k = 3
#
# 输出： 2
#
# 解释：
#
#
#
# 有效的子集有：
#
# {1, 2}：节点 1 和 2 都是节点 0 的子节点，且彼此不直接相连。它们的值之和为 1 + 2 = 3 ，可以被 3 整除。
# {2, 3}：节点 2 和 3 也不相邻。它们的值之和为 2 + 1 = 3 ，可以被 3 整除。
# 没有其他子集同时满足两个条件。因此，答案是 2 。
#
#
#
# 提示：
#
# n == parent.length == nums.length
# 1 <= n <= 1000
# parent[0] == -1
# 对于所有的 1 <= i < n：
# 0 <= parent[i] < i
# 1 <= nums[i] <= 109
# 1 <= k <= 100
# parent 表示一棵有效的有根树。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        g = defaultdict(list)
        for i, x in enumerate(parent):
            g[x].append(i)

        @cache
        def dfs(x, st):  # 以x为根的子树，st=0表示不选x，st=1表示不限制选x，返回各自余数的子集个数
            res = [0] * k
            r1 = [0] * k
            r1[0] = 1  # 表示一个都不选
            if len(g[x]) == 0:
                res[0] = 1
                if st == 0:
                    return res
                res[nums[x] % k] += 1
                return res
            for y in g[x]:
                r2 = dfs(y, 1)
                for i in range(k):
                    for j in range(k):
                        res[(i + j) % k] += r1[i] * r2[j]
                        res[(i + j) % k] %= MOD
                r1, res = res, [0] * k

            res = r1[:]
            if st == 0:
                # print(x, st, r1)
                return r1
            res1 = [0] * k
            r1 = [0] * k
            r1[nums[x] % k] = 1  # 表示之选一个x
            for y in g[x]:
                r2 = dfs(y, 0)
                for i in range(k):
                    for j in range(k):
                        res1[(i + j) % k] += r1[i] * r2[j]
                        res1[(i + j) % k] %= MOD
                r1, res1 = res1, [0] * k

            # print(x, st, res, res1)
            return [res[i] + r1[i] for i in range(k)]
        ans = dfs(0, 1)
        return (ans[0] - 1) % MOD  # 减去一个空子集的情况



so = Solution()
print(so.countValidSubsets(parent = [-1,0], nums = [200,7], k = 8))
print(so.countValidSubsets(parent = [-1,0,0,0], nums = [2,1,2,1], k = 3))
print(so.countValidSubsets(parent = [-1,0,1], nums = [1,2,3], k = 3))




