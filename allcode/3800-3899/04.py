

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        left = list(range(1, n + 1))
        right = list(range(n, 0, -1))
        stack = []
        for i, x in enumerate(nums):
            while stack and (stack[-1][1] | x) != stack[-1][1]:
                j, y = stack.pop()
                right[j] = i - j
            stack.append([i, x])

        stack = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and ((stack[-1][1] | x) != stack[-1][1] or stack[-1][1] == x):
                j, y = stack.pop()
                left[j] = j - i
            stack.append([i, x])

        # print(left, right)
        ans = 0
        for i in range(n):
            ans += left[i] * right[i]

        return ans



so = Solution()
print(so.countGoodSubarrays([2,2,3]))
print(so.countGoodSubarrays([4,2,3]))




