

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counter = Counter()
        ans = []
        for x in nums:
            if counter[x] < k:
                ans.append(x)
                counter[x] += 1
        return ans


so = Solution()
print(so.limitOccurrences(nums = [1,1,1,2,2,3], k = 2))




