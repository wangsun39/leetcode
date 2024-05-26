
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((x + 1) // 2 for x in coins)


so = Solution()




