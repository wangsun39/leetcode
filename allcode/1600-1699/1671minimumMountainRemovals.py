

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        def proc(l):  # 返回每个nums[i]左侧能构成最长的单调增数组的长度
            dp = [0] * n
            for i, x in enumerate(l[1:], 1):
                for j in range(i):
                    if l[j] < x:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp
        left = proc(nums)
        right = proc(nums[::-1])[::-1]
        ans = 0  # 山形数组最大长度
        for i in range(n):
            if left[i] and right[i]:
                ans = max(ans, left[i] + right[i] + 1)
        return n - ans


so = Solution()
print(so.minimumMountainRemovals([2,1,1,5,6,2,3,1]))
print(so.minimumMountainRemovals([1,3,1]))




