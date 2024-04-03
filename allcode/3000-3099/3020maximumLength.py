

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        ans = 1
        if counter[1]:
            ans = max(ans, counter[1] if counter[1] & 1 else counter[1] - 1)
        for x in nums:
            if x == 1: continue
            s = set()
            y = x
            while y in counter and counter[y] >= 2:
                s.add(y)
                y = y * y
            if counter[y] == 1:
                ans = max(ans, len(s) * 2 + 1)
            else:
                ans = max(ans, len(s) * 2 - 1)
        return ans

so = Solution()
print(so.maximumLength([14,14,196,196,38416,38416]))
print(so.maximumLength([1,1]))
print(so.maximumLength([5,4,1,2,2]))
print(so.maximumLength([1,3,2,4]))




