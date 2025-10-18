# 给你一个数组 nums ，它是 [0, 1, 2, ..., n - 1] 的一个排列 。对于任意一个 [0, 1, 2, ..., n - 1] 的排列 perm ，其 分数 定义为：
#
# score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|
#
# 返回具有 最低 分数的排列 perm 。如果存在多个满足题意且分数相等的排列，则返回其中字典序最小的一个。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,2]
#
# 输出：[0,1,2]
#
# 解释：
#
#
#
# 字典序最小且分数最低的排列是 [0,1,2]。这个排列的分数是 |0 - 0| + |1 - 2| + |2 - 1| = 2 。
#
# 示例 2：
#
# 输入：nums = [0,2,1]
#
# 输出：[0,2,1]
#
# 解释：
#
#
#
# 字典序最小且分数最低的排列是 [0,2,1]。这个排列的分数是 |0 - 1| + |2 - 2| + |1 - 0| = 2 。
#
#
#
# 提示：
#
# 2 <= n == nums.length <= 14
# nums 是 [0, 1, 2, ..., n - 1] 的一个排列。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        @cache
        def dfs(mask, pre):
            # 排列P，已选的下标mask，p[start-1]处选择的值pre
            if mask.bit_count() == n: return abs(pre - nums[0]), []
            res = inf
            for i in range(n):
                if mask & (1 << i) == 0:
                    r, arr = dfs(mask | (1 << i), i)
                    if r + abs(pre - nums[i]) < res:
                        res = r + abs(pre - nums[i])
                        v = [i] + arr
            return res, v

        _, ans = dfs(1, 0)
        return [0] + ans



so = Solution()
print(so.findPermutation([0,2,1]))
print(so.findPermutation([1,0,2]))




