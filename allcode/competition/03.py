

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        values = list(counter.values())
        mn, mx = min(values), max(values)
        ans = inf
        for i in range(mn, mx + 1):  # 枚举最终最小频率值
            cur = 0
            for x in values:
                if x < i:
                    cur += x
                elif x > i + k:
                    cur += (x - (i + k))
            ans = min(ans, cur)
        return ans


so = Solution()
print(so.minimumDeletions(word = "aabcaba", k = 0))
print(so.minimumDeletions(word = "dabdcbdcdcd", k = 2))
print(so.minimumDeletions(word = "aaabaaa", k = 2))




