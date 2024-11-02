# 给你一个整数数组 nums 和一个整数 k 。请你向 nums 中追加 k 个 未 出现在 nums 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
#
# 返回追加到 nums 中的 k 个整数之和。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,25,10,25], k = 2
# 输出：5
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。
# nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
# 示例 2：
#
# 输入：nums = [5,6], k = 6
# 输出：25
# 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。
# nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。
# 所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.insert(0, 0)
        ans = 0
        for x, y in pairwise(nums):
            if y - x <= 1: continue
            if k > y - x - 1:
                k -= (y - x - 1)
                ans += (x + y) * (y - x - 1) // 2
            else:
                ans += (x + 1) * k + k * (k - 1) // 2  # 等差求和公式
                return ans
        ans += (y + 1) * k + k * (k - 1) // 2
        return ans



so = Solution()

print(so.minimalKSum(nums = [5,6], k = 6))  # 25
print(so.minimalKSum(nums = [1,4,25,10,25], k = 2))  # 5




