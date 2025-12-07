

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        s = [0]
        # for i in range(n):
        #     di, ri = damage[i], requirement[i]
        #     s.append(s[-1] + di - ri)
        s = list(accumulate(damage, initial=0))
        ans = 0
        j = 0
        for i in range(n):
            while j < n and hp >= s[j + 1] - s[i] + requirement[j]:
                j += 1
            ans += j - i
        return ans



so = Solution()
print(so.totalScore(hp = 11, damage = [3,6,7], requirement = [4,2,5]))




