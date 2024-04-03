

from leetcode.allcode.competition.mypackage import *

class Solution:
        def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
            empty = drink = 0
            while True:
                drink += numBottles
                empty += numBottles
                if empty >= numExchange:
                    numBottles = 1
                    empty -= numExchange
                    numExchange += 1
                else:
                    return drink



so = Solution()
print(so.maxBottlesDrunk(numBottles = 13, numExchange = 6))
print(so.maxBottlesDrunk(numBottles = 10, numExchange = 3))




