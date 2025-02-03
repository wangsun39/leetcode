# 给你一个大小为 n下标从 0开始的整数数组nums和一个正整数k。
#
# 对于k <= i < n - k之间的一个下标i，如果它满足以下条件，我们就称它为一个好下标：
#
# 下标 i 之前 的 k个元素是 非递增的。
# 下标 i 之后的 k个元素是 非递减的。
# 按 升序返回所有好下标。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,1,1,3,4,1], k = 2
# 输出：[2,3]
# 解释：数组中有两个好下标：
# - 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
# - 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
# 注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
# 示例 2：
#
# 输入：nums = [2,1,1,2], k = 2
# 输出：[]
# 解释：数组中没有好下标。
#
#
# 提示：
#
# n == nums.length
# 3 <= n <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= n / 2
#
# https://leetcode.cn/problems/find-all-good-indices

from leetcode.allcode.competition.mypackage import *

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        nums1 = []
        n = len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 0:
                nums1.append(0)
            elif nums[i] - nums[i - 1] > 0:
                nums1.append(1)
            elif nums[i] - nums[i - 1] < 0:
                nums1.append(-1)
        print(nums1)
        stack1 = [-1]
        cur = -1
        for i in range(n - 1):
            stack1.append(cur)
            if nums1[i] == 1:
                cur = i + 1
        print(stack1)
        stack2 = [10000000]
        cur = 10000000
        for i in range(n - 2, -1, -1):
            stack2.insert(0, cur)
            if nums1[i] == -1:
                cur = i
        print(stack2)
        ans = []
        for i in range(k, n - k):
            if i - stack1[i] >= k and stack2[i] - i >= k:
                ans.append(i)
        return ans


so = Solution()
print(so.goodIndices(nums = [877464,394689,51354,348332,285490,570624], k = 2))
print(so.goodIndices(nums = [2,1,1,1,3,4,1], k = 2))
print(so.goodIndices(nums = [2,1,1,2], k = 2))




