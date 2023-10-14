

from leetcode.allcode.competition.mypackage import *

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money - prices[0] - prices[1] >= 0:
            return money - prices[0] - prices[1]
        return money


so = Solution()
print(so.buyChoco(prices = [1,2,2], money = 3))
print(so.buyChoco(prices = [3,2,3], money = 3))




