# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [21,4,7]
# 输出：32
# 解释：
# 21 有 4 个因数：1, 3, 7, 21
# 4 有 3 个因数：1, 2, 4
# 7 有 2 个因数：1, 7
# 答案仅为 21 的所有因数的和。
# 示例 2:
#
# 输入: nums = [21,21]
# 输出: 64
# 示例 3:
#
# 输入: nums = [1,2,3,4,5]
# 输出: 0
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = len(nums)
        def factor(x):
            res = []
            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    res.append(i)
                    if x // i != i:
                        res.append(x // i)
                if len(res) > 4:
                    return False
            if len(res) == 4:
                return sum(res)
            return 0
        return sum(factor(x) for x in nums)


so = Solution()
print(so.sumFourDivisors([21,4,7]))
print(so.sumFourDivisors([21,21]))
print(so.sumFourDivisors([1,2,3,4,5]))




