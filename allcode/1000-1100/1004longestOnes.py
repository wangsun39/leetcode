# 给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 示例 2：
#
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1
# 0 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = []
        n = len(nums)
        for i, x in enumerate(nums):
            if x == 0:
                zeros.append(i)
        zeros = [-1] + zeros + [n]  # 哨兵
        if len(zeros) - 2 <= k:
            return n
        ans = 0
        for i in range(1, len(zeros) - k):
            lo = zeros[i - 1] + 1
            hi = zeros[i + k]
            ans = max(ans, hi - lo)
        return ans


obj = Solution()
print(obj.longestOnes(nums = [0,0,0,1], k = 4))
print(obj.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1], k = 0))
print(obj.longestOnes(nums = [0,0,1,1], k = 1))
print(obj.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))

