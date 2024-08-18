

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = energyDrinkA[0]
        dp2[0] = energyDrinkB[0]
        for i in range(1, n):
            dp1[i] = dp1[i - 1] + energyDrinkA[i]
            if i > 1 and dp1[i] < dp2[i - 2] + energyDrinkA[i]:
                dp1[i] = dp2[i - 2] + energyDrinkA[i]
            dp2[i] = dp2[i - 1] + energyDrinkB[i]
            if i > 1 and dp2[i] < dp1[i - 2] + energyDrinkB[i]:
                dp2[i] = dp1[i - 2] + energyDrinkB[i]
        return max(dp1[-1], dp2[-1])



so = Solution()
print(so.maxEnergyBoost(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]))
print(so.maxEnergyBoost(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]))
print(so.maxEnergyBoost(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]))




