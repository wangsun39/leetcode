# 给你一个整数数组 nums，请你将该数组升序排列。
#
# 你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortArray(self, nums):
        n = len(nums)
        ans = [0] * n
        def dfs(arr):
            m = len(arr)
            if m == 1:
                return arr
            l1 = dfs(arr[:m//2])
            l2 = dfs(arr[m//2:])
            res = [0] * m
            i = j = k = 0
            while i < len(l1) or j < len(l2):
                if i < len(l1) and j < len(l2):
                    if l1[i] < l2[j]:
                        res[k] = l1[i]
                        i += 1
                    else:
                        res[k] = l2[j]
                        j += 1
                elif i < len(l1):
                    res[k] = l1[i]
                    i += 1
                else:
                    res[k] = l2[j]
                    j += 1
                k += 1
            return res
        return dfs(nums)


so = Solution()
print(so.sortArray([5,2,3,1]))
print(so.sortArray([5,1,1,2,0,0]))