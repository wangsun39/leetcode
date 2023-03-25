# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
#
# 一个子数组指的是原数组中连续的一个子序列。
#
# 请你返回满足题目要求的最短子数组的长度。
#
#
#
# 示例 1：
#
# 输入：arr = [1,2,3,10,4,2,3,5]
# 输出：3
# 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
# 另一个正确的解为删除子数组 [3,10,4] 。
# 示例 2：
#
# 输入：arr = [5,4,3,2,1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
# 示例 3：
#
# 输入：arr = [1,2,3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。
# 示例 4：
#
# 输入：arr = [1]
# 输出：0
#
#
# 提示：
#
# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9


from typing import Optional
from collections import deque
# Definition for a binary tree node.
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r, n = -1, 0, len(arr)
        for i, x in enumerate(arr[1:], 1):
            if arr[i - 1] > x:
                if l == -1:
                    l = i - 1
                r = i
        if arr[l] <= arr[r]:  # 删除 [l + 1, r - 1]
            return r - 1 - l
        ans = min(n - l - 1, r)
        j = n - 1
        for i in range(l, -1, -1):
            while j >= r and arr[i] <= arr[j]:
                ans = min(ans, j - 1 - i)
                j -= 1
        return ans





so = Solution()
print(so.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]))
print(so.findLengthOfShortestSubarray(arr = [22,37,59,16,42,32,29,53,9,55,29,3,4,1,49,17,37,31,27,45,33,24,54,51,32,51,54,31,36,53]))
print(so.findLengthOfShortestSubarray(arr = [1,2,3]))
print(so.findLengthOfShortestSubarray(arr = [5,4,3,2,1]))





