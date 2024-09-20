

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for k, v in counter.items():
            if v == 1 and k - 1 not in counter and k + 1 not in counter:
                ans.append(k)
        return ans


so = Solution()
print(so.findLonely([10,6,5,8]))




