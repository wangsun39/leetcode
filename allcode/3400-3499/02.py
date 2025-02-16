

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas) // 4
        pizzas.sort(reverse=True)
        odds = (n + 1) // 2
        ans = sum(pizzas[:odds])
        even = n - odds
        for i in range(odds + 1, 4 * n, 2):
            if even == 0: break
            ans += pizzas[i]
            even -= 1
        return ans


so = Solution()
print(so.maxWeight(pizzas = [1,2,3,4,5,6,7,8]))
print(so.maxWeight(pizzas = [2,1,1,1,1,1,1,1]))




