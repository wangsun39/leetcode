# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
#
# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
#
# 如果一个节点有 0 个子节点，那么该节点为叶节点。
#
#
#
# 示例 1：
#
#
# 输入：arr = [6,2,4]
# 输出：32
# 解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。
# 示例 2：
#
#
# 输入：arr = [4,11]
# 输出：44
#
#
# 提示：
#
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# 答案保证是一个 32 位带符号整数，即小于 231 。
from functools import cache
from math import inf
from typing import List
from collections import deque, defaultdict


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        seg_max = [[0] * n for _ in range(n)]  # min_max[i][j] 表示区间 [i, j] 上的arr最大值
        for i in range(n):
            cur_mn, cur_mx = inf, -inf
            for j in range(i, n):
                seg_max[i][j] = cur_mx = max(arr[j], cur_mx)

        @cache
        def dfs(x, y):  # 获取 区间 [x, y] 上的非叶节点的值的最小可能总和
            if x == y:
                return 0
            res = inf
            for i in range(x, y):
                res = min(res, dfs(x, i) + dfs(i + 1, y) + seg_max[x][i] * seg_max[i + 1][y])
            # print(x, y, res)
            return res

        return dfs(0, n - 1)




obj = Solution()
print(obj.mctFromLeafValues(arr = [6,2,4]))
print(obj.mctFromLeafValues(arr = [4,11]))

