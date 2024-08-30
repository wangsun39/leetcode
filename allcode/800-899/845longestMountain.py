# 把符合下列属性的数组 arr 称为 山脉数组 ：
#
# arr.length >= 3
# 存在下标 i（0 < i < arr.length - 1），满足
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
#
#
#
# 示例 1：
#
# 输入：arr = [2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
# 示例 2：
#
# 输入：arr = [2,2,2]
# 输出：0
# 解释：不存在山脉子数组。
#
#
# 提示：
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
#
#
# 进阶：
#
# 你可以仅用一趟扫描解决此问题吗？
# 你可以用 O(1) 空间解决此问题吗？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n  # 左边最长的递增子数组
        right = [0] * n
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
        if sum(1 for i in range(n) if left[i] == 0 or right[i] == 0) == n:
            return 0
        return max(left[i] + right[i] + 1 for i in range(n) if left[i] and right[i])


so = Solution()
print(so.longestMountain(arr = [0,1,2,3,4,5,6,7,8,9]))
print(so.longestMountain(arr = [2,3]))
print(so.longestMountain(arr = [2,1,4,7,3,2,5]))
print(so.longestMountain(arr = [2,2,2]))




