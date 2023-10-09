# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。
#
# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
#
# 子数组是数组的一个 连续 部分。
#
#
#
# 示例 1：
#
# 输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
# 示例 2：
#
# 输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
# 示例 3：
#
# 输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
#
#
# 提示：
#
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from collections import defaultdict
from itertools import accumulate
from typing import List
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n  # 分别表示nums[:i] 和nums[i:] 中长度为 firstLen 的区间和最大值
        cur = left[firstLen - 1] = sum(nums[:firstLen])
        for i in range(firstLen, n):
            cur = cur - nums[i - firstLen] + nums[i]
            left[i] = max(left[i - 1], cur)
        cur = right[n - firstLen] = sum(nums[n - firstLen:])
        for i in range(n - firstLen - 1, -1, -1):
            cur = cur - nums[i + firstLen] + nums[i]
            right[i] = max(right[i + 1], cur)
        # print(left,right)
        cur = sum(nums[:secondLen])
        ans = cur + right[secondLen]
        for i in range(1, n - secondLen + 1):
            cur = cur - nums[i - 1] + nums[i + secondLen - 1]
            ans = max(ans, cur + left[i - 1])
            if i + secondLen < n:
                ans = max(ans, cur + right[i + secondLen])
        return ans



obj = Solution()
print(obj.maxSumTwoNoOverlap(nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3))
print(obj.maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2))
print(obj.maxSumTwoNoOverlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2))

