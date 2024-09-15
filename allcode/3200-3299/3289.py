

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 2:
                ans.append(k)
        return ans


so = Solution()
print(so.getSneakyNumbers())




