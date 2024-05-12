

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1 = {v: k for k, v in enumerate(s)}
        d2 = {v: k for k, v in enumerate(t)}
        return sum(abs(d1[k] - d2[k]) for k in d1.keys())


so = Solution()
print(so.findPermutationDifference(s = "abc", t = "bac"))
print(so.findPermutationDifference(s = "abcde", t = "edbac"))




