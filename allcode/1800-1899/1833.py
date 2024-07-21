

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s = list(accumulate(costs, initial=0))
        p = bisect_right(s, coins)
        return p - 1



so = Solution()
print(so.maxIceCream(costs = [1,3,2,4,1], coins = 7))
print(so.maxIceCream(costs = [10,6,8,7,7,8], coins = 5))
print(so.maxIceCream(costs = [1,6,3,1,2,5], coins = 20))




