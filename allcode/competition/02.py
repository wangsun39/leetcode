

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i, x in enumerate(happiness[:k]):
            if x > i:
                x -= i
                ans += x
            else:
                break
        return ans


so = Solution()
print(so.maximumHappinessSum(happiness = [1,2,3], k = 2))
print(so.maximumHappinessSum(happiness = [1,1,1,1], k = 2))
print(so.maximumHappinessSum(happiness = [2,3,4,5], k = 1))




