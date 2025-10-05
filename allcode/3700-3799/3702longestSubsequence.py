

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        v = reduce(lambda x, y: x ^ y, nums)
        if v: return n
        if all(x == 0 for x in nums): return 0
        return n - 1



so = Solution()
print(so.longestSubsequence([1,1,1,1]))
print(so.longestSubsequence([6,7,3]))
print(so.longestSubsequence([0,2,14]))
print(so.longestSubsequence([1,2,3]))




