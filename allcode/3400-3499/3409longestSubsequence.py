

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        dp = [[0] * 301 for _ in range(2)]
        i, j = 0, 1
        for x in nums:
            for i in range(1, 300):


so = Solution()
print(so.longestSubsequence())




