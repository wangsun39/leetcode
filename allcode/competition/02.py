

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [x % 24 for x in hours]
        counter = Counter(hours)
        ans = 0
        for k in range(13):
            if k not in counter: continue
            v = counter[k]
            if k == 0 or k == 12:
                ans += v * (v - 1) // 2
            elif 24 - k in counter:
                ans += counter[24 - k] * v
        return ans


so = Solution()
print(so.countCompleteDayPairs([21,19,3]))
print(so.countCompleteDayPairs([12,12,30,24,24]))
print(so.countCompleteDayPairs([72,48,24,3]))
print(so.countCompleteDayPairs([11,11,24]))




