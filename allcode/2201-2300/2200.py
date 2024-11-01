

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)
        for i, x in enumerate(nums):
            if x != key: continue
            mn = max(0, i - k)
            mx = min(n - 1, i + k)
            if ans:
                mn = max(mn, ans[-1] + 1)
            for j in range(mn, mx + 1):
                ans.append(j)
            if ans[-1] == n - 1:
                break
        return ans



so = Solution()
print(so.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))




