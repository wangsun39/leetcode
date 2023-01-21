import bisect
import math
from typing import List
class Solution:
    def lengthOfLIS1(self, nums):
        number = len(nums)
        if number == 0:
            return 0
        A = [0] * number
        A[0] = 1
        # A[i] 表示以nums[i]结尾的最大字序长度
        for i in range(1, number):
            if nums[i] == nums[i-1]:
                A[i] = A[i-1]
            else:
                max_v = 1
                for j in range(i):
                    #print(max_v, i, j)
                    if nums[i] > nums[j]:
                        max_v = max(max_v, A[j]+1)
                A[i] = max_v
        print(A)
        return max(A)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 2023/1/20  一维DP  O(n^2)
        n = len(nums)
        dp = [1] * n  # dp[i] 表示以 nums[:i+1] 中的最长递增子序列长度
        for i, x in enumerate(nums):
            cur_mx = 1
            for j in range(i):
                if x > nums[j]:
                    cur_mx = max(cur_mx, dp[j] + 1)
            dp[i] = cur_mx
        return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 2023/1/20  单调栈 + 二分  O(nlogn)
        stack = [nums[0]]  # 单调栈
        for i, x in enumerate(nums):
            if len(stack) == 0 or x > stack[-1]:
                stack.append(x)
                continue
            pos = bisect.bisect_left(stack, x)
            stack[pos] = x
        return len(stack)




so = Solution()
print(so.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(so.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

