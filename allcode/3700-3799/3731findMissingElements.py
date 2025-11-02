

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        s = set(nums)
        ans = []
        for i in range(mn + 1, mx):
            if i not in s:
                ans.append(i)
        return ans


so = Solution()
print(so.findMissingElements([1,4,2,5]))




