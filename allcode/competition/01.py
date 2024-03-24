

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            counter = Counter()
            for j in range(i, n + 1):
                ans = max(ans, j - i)
                if j > n - 1: break
                counter[s[j]] += 1
                if counter[s[j]] > 2:
                    break

        return ans


so = Solution()
print(so.maximumLengthSubstring("bcbbbcba"))
print(so.maximumLengthSubstring("aaaa"))




