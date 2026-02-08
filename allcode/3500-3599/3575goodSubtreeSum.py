# 给你一个根节点为 0 的无向树，包含 n 个节点，编号从 0 到 n - 1。每个节点 i 都有一个整数值 vals[i]，其父节点为 par[i] 。
#
# 从一个节点 子树 内选取部分节点，它们的数值组成一个 子集 ，如果所选数值的十进制表示中，从 0 到 9 每个数字在所有数的数位最多出现一次，那么我们称它是 好 子集。
#
# 一个好子集的 分数 是其节点值的总和。
#
# 定义一个长度为 n 的数组 maxScore，其中 maxScore[u] 表示以节点 u 为根的子树（包括 u 本身及其所有后代）中，好子集的最大可能值总和。
#
# 返回 maxScore 中所有值的总和。
#
# 由于答案可能很大，请将其对 109 + 7 取模 后返回。
#
# 数组的 子集 是选取数组中元素得到的集合（可能为空）。
#
#
#
# 示例 1:
#
# 输入: vals = [2,3], par = [-1,0]
#
# 输出: 8
#
# 解释:
#
#
#
# 以节点 0 为根的子树包括节点 {0, 1}。子集 {2, 3} 是 好的，因为数字 2 和 3 只出现一次。此子集的分数是 2 + 3 = 5。
# 以节点 1 为根的子树只包括节点 {1}。子集 {3} 是 好的。此子集的分数是 3。
# maxScore 数组为 [5, 3]，并且 maxScore 中所有值的总和是 5 + 3 = 8。因此，答案是 8。
# 示例 2:
#
# 输入: vals = [1,5,2], par = [-1,0,0]
#
# 输出: 15
#
# 解释:
#
#
#
# 以节点 0 为根的子树包括节点 {0, 1, 2}。子集 {1, 5, 2} 是 好的，因为数字 1、5 和 2 只出现一次。此子集的分数是 1 + 5 + 2 = 8。
# 以节点 1 为根的子树只包括节点 {1}。子集 {5} 是 好的。此子集的分数是 5。
# 以节点 2 为根的子树只包括节点 {2}。子集 {2} 是 好的。此子集的分数是 2。
# maxScore 数组为 [8, 5, 2]，并且 maxScore 中所有值的总和是 8 + 5 + 2 = 15。因此，答案是 15。
# 示例 3:
#
# 输入: vals = [34,1,2], par = [-1,0,1]
#
# 输出: 42
#
# 解释:
#
#
#
# 以节点 0 为根的子树包括节点 {0, 1, 2}。子集 {34, 1, 2} 是 好的，因为数字 3、4、1 和 2 只出现一次。此子集的分数是 34 + 1 + 2 = 37。
# 以节点 1 为根的子树包括节点 {1, 2}。子集 {1, 2} 是 好的，因为数字 1 和 2 只出现一次。此子集的分数是 1 + 2 = 3。
# 以节点 2 为根的子树只包括节点 {2}。子集 {2} 是 好的。此子集的分数是 2。
# maxScore 数组为 [37, 3, 2]，并且 maxScore 中所有值的总和是 37 + 3 + 2 = 42。因此，答案是 42。
# 示例 4:
#
# 输入: vals = [3,22,5], par = [-1,0,1]
#
# 输出: 18
#
# 解释:
#
# 以节点 0 为根的子树包括节点 {0, 1, 2}。子集 {3, 22, 5} 不是好子集，因为数字 2 出现两次。子集 {3, 5} 是好子集，此子集的分数是 3 + 5 = 8。
# 以节点 1 为根的子树包括节点 {1, 2}。子集 {22, 5} 不是好子集，因为数字 2 出现两次。子集 {5} 是好子集，此子集的分数是 5。
# 以节点 2 为根的子树包括 {2}。子集 {5} 是 好的。此子集的分数是 5。
# maxScore 数组为 [8, 5, 5]，并且 maxScore 中所有值的总和是 8 + 5 + 5 = 18。因此，答案是 18。
#
#
# 提示:
#
# 1 <= n == vals.length <= 500
# 1 <= vals[i] <= 109
# par.length == n
# par[0] == -1
# 对于 [1, n - 1] 中的每一个 i ，都有 0 <= par[i] < n 。
# 输入生成保证父数组 par 表示一棵有效的树。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def goodSubtreeSum1(self, vals: List[int], par: List[int]) -> int:
        # 这个方法正确，但性能不够，被卡常了
        MOD = 10 ** 9 + 7
        n = len(vals)
        g = defaultdict(list)
        for i, x in enumerate(par):
            g[x].append(i)

        def to_mask(x):
            s = str(x)
            res = 0
            for y in s:
                if res & (1 << int(y)):  # 此数不能选
                    return 0
                res |= (1 << int(y))
            return res

        mask = [to_mask(x) for x in vals]
        p_mx = [0] * n  # 以 i 为根的子树的最大分数

        def dfs(x):
            res = [0] * 1024
            mask_x = mask[x]
            if mask_x: res[mask_x] = vals[x]
            if len(g[x]) == 0:
                p_mx[x] = max(res)
                return res

            v = [0] * 1024
            for y in g[x]:
                res_y = dfs(y)
                for i in range(1024):
                    ii = 1023 & (~i)
                    j = ii
                    while j:
                        # 处理 sub 的逻辑
                        v[i | j] = max(v[i | j], res[i] + res_y[j])
                        j = (j - 1) & ii
                res = v[:]
            p_mx[x] = max(res)
            return res

        dfs(0)
        # print(p_mx)
        # ans = 0
        def dfs2(x):
            # nonlocal ans
            res = p_mx[x]
            for y in g[x]:
                res += dfs2(y)
                res %= MOD
            return res

        return dfs2(0)



    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(vals)
        g = defaultdict(list)
        for i, x in enumerate(par):
            g[x].append(i)

        def to_mask(x):
            s = str(x)
            res = 0
            for y in s:
                if res & (1 << int(y)):  # 此数不能选
                    return 0
                res |= (1 << int(y))
            return res

        mask = [to_mask(x) for x in vals]
        p_mx = [0] * n  # 以 i 为根的子树的最大分数

        def dfs(x):
            res = {0: 0}
            mask_x = mask[x]
            if mask_x: res[mask_x] = vals[x]
            if len(g[x]) == 0:
                p_mx[x] = max(res.values())
                return res

            v = {0: 0}
            for y in g[x]:
                res_y = dfs(y)
                for i, iv in res.items():
                    for j, jy in res_y.items():
                        if (i & j) == 0:
                            v[i | j] = max(v.get(i | j, 0), res[i] + res_y[j])
                res = dict(v)
            if res: p_mx[x] = max(res.values())
            return res

        dfs(0)
        def dfs2(x):
            res = p_mx[x]
            for y in g[x]:
                res += dfs2(y)
                res %= MOD
            return res

        return dfs2(0)



so = Solution()
print(so.goodSubtreeSum(vals = [3,22,5], par = [-1,0,1]))
print(so.goodSubtreeSum(vals = [345672,735649,125748,462830,8210,369107,348052,31957], par = [-1,5,3,0,3,4,0,6]))
print(so.goodSubtreeSum(vals = [2,3], par = [-1,0]))
