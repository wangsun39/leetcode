# 给你一个整数数组 nums 。数组 nums 的 唯一性数组 是一个按元素从小到大排序的数组，包含了 nums 的所有
# 非空子数组中
# 不同元素的个数。
#
# 换句话说，这是由所有 0 <= i <= j < nums.length 的 distinct(nums[i..j]) 组成的递增数组。
#
# 其中，distinct(nums[i..j]) 表示从下标 i 到下标 j 的子数组中不同元素的数量。
#
# 返回 nums 唯一性数组 的 中位数 。
#
# 注意，数组的 中位数 定义为有序数组的中间元素。如果有两个中间元素，则取值较小的那个。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
#
# 输出：1
#
# 解释：
#
# nums 的唯一性数组为 [distinct(nums[0..0]), distinct(nums[1..1]), distinct(nums[2..2]), distinct(nums[0..1]), distinct(nums[1..2]), distinct(nums[0..2])]，即 [1, 1, 1, 2, 2, 3] 。唯一性数组的中位数为 1 ，因此答案是 1 。
#
# 示例 2：
#
# 输入：nums = [3,4,3,4,5]
#
# 输出：2
#
# 解释：
#
# nums 的唯一性数组为 [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3] 。唯一性数组的中位数为 2 ，因此答案是 2 。
#
# 示例 3：
#
# 输入：nums = [4,3,5,4]
#
# 输出：2
#
# 解释：
#
# nums 的唯一性数组为 [1, 1, 1, 1, 2, 2, 2, 3, 3, 3] 。唯一性数组的中位数为 2 ，因此答案是 2 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        N = n * (n + 1) // 2  # 非空子数组个数
        def check(val):
            # 检查不同元素个数<=val的子数组个数是否>= (N + 1) // 2
            # 最小满足这个函数的数，就是答案
            r = 0
            s = {}
            res = 0
            for l in range(n):
                while r < n and len(s) <= val:
                    if nums[r] in s:
                        s[nums[r]] += 1
                    else:
                        s[nums[r]] = 1
                    r += 1
                if len(s) > val:
                    res += (r - l - 1)
                else:
                    res += (r - l)
                if s[nums[l]] == 1:
                    del(s[nums[l]])
                else:
                    s[nums[l]] -= 1

            return res >= (N + 1) // 2

        lo, hi = 1, len(set(nums))
        if check(lo): return lo
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.medianOfUniquenessArray(nums = [91,64,76,18,61,55,46,93,65,99]))
print(so.medianOfUniquenessArray(nums = [3,4,3,4,5]))
print(so.medianOfUniquenessArray(nums = [1,2,3]))




