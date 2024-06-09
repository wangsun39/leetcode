

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        ss = SortedSet()
        rewardValues.sort()
        for x in rewardValues:
            p = ss.bisect_right(x - 1)
            if p == 0:
                ss.add(x)
            else:
                s = {x}
                for i in range(p):
                    s.add(ss[i] + x)
                for y in s:
                    ss.add(y)
        return ss[-1]



so = Solution()
print(so.maxTotalReward(rewardValues =  [1,10,9])),
print(so.maxTotalReward(rewardValues =  [1,6,4,3,2]))
print(so.maxTotalReward(rewardValues = [1,1,3,3]))




