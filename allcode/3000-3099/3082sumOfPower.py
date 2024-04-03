# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
#
# 一个整数数组的 能量 定义为和 等于 k 的子序列的数目。
#
# 请你返回 nums 中所有子序列的 能量和 。
#
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,3], k = 3
#
# 输出： 6
#
# 解释：
#
# 总共有 5 个能量不为 0 的子序列：
#
# 子序列 [1,2,3] 有 2 个和为 3 的子序列：[1,2,3] 和 [1,2,3] 。
# 子序列 [1,2,3] 有 1 个和为 3 的子序列：[1,2,3] 。
# 子序列 [1,2,3] 有 1 个和为 3 的子序列：[1,2,3] 。
# 子序列 [1,2,3] 有 1 个和为 3 的子序列：[1,2,3] 。
# 子序列 [1,2,3] 有 1 个和为 3 的子序列：[1,2,3] 。
# 所以答案为 2 + 1 + 1 + 1 + 1 = 6 。
#
# 示例 2：
#
# 输入： nums = [2,3,3], k = 5
#
# 输出： 4
#
# 解释：
#
# 总共有 3 个能量不为 0 的子序列：
#
# 子序列 [2,3,3] 有 2 个子序列和为 5 ：[2,3,3] 和 [2,3,3] 。
# 子序列 [2,3,3] 有 1 个子序列和为 5 ：[2,3,3] 。
# 子序列 [2,3,3] 有 1 个子序列和为 5 ：[2,3,3] 。
# 所以答案为 2 + 1 + 1 = 4 。
#
# 示例 3：
#
# 输入： nums = [1,2,3], k = 7
#
# 输出： 0
#
# 解释：不存在和为 7 的子序列，所以 nums 的能量和为 0 。
#
#
#
# 提示：
#
# 1 <= n <= 100
# 1 <= nums[i] <= 104
# 1 <= k <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:

    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dfs(start, num, target):  # 从start开始，选num个数，目标和是target，返回总数
            # 隐含条件num<=target，否则数量为0
            if start == n - 1:
                return target == nums[-1] and num == 1

            r1 = dfs(start + 1, num, target)
            r2 = 0
            if target > nums[start] and num > 1:
                r2 = dfs(start + 1, num - 1, target - nums[start])
            elif target == nums[start] and num == 1:
                r2 = 1
            # print(start, target, r1 + r2)
            return r1 + r2

        ans = 0
        for i in range(1, k + 1):
            n_sub = dfs(0, i, k)
            ans += ((n_sub % MOD) * pow(2, n - i, MOD) % MOD)
            ans %= MOD
        return ans



so = Solution()
print(so.sumOfPower(nums = [2,3,3], k = 5))  # 4
print(so.sumOfPower([2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1], 49))  # 999634217
print(so.sumOfPower([1,1,2,3,3], 5))  # 24
print(so.sumOfPower(nums = [5,5,6], k = 5))  # 8
print(so.sumOfPower(nums = [1,2,3], k = 3))  # 6
print(so.sumOfPower(nums = [1,2,3], k = 7))  # 0




