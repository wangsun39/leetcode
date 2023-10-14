
from leetcode.allcode.competition.mypackage import *


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        s1 = sum(reward1)
        diff = [reward2[i] - reward1[i] for i in range(n)]
        diff.sort(reverse=True)
        # print(s1)
        # print(diff)

        return s1 + sum(diff[:n - k])


so = Solution()
print(so.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))
print(so.miceAndCheese([4,1,5,3,3],[3,4,4,5,2],3))
print(so.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2))




