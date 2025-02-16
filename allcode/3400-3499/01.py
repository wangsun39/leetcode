

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            counter = Counter(s[i: i + k])
            if len(counter.keys()) != 1: continue
            if i > 0 and s[i] == s[i - 1]: continue
            if i + k <= n - 1 and s[i + k - 1] == s[i + k]: continue
            return True
        return False

so = Solution()
print(so.hasSpecialSubstring(s = "aaabaaa", k = 3))
print(so.hasSpecialSubstring(s = "abc", k = 2))




