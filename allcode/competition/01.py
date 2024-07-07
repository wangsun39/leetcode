

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        s += s
        return s[k: k + n]


so = Solution()
print(so.getEncryptedString(s = "dart", k = 3))
print(so.getEncryptedString(s = "aaa", k = 1))
print(so.getEncryptedString(s = "dart", k = 3))




