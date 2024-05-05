

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        l = []
        n = len(word)
        for i in range(0, n, k):
            l.append(word[i: i + k])
        counter = Counter(l)
        mx = counter.most_common(1)[0][1]
        return n // k - mx


so = Solution()
print(so.minimumOperationsToMakeKPeriodic(word = "leetcodeleet", k = 4))
print(so.minimumOperationsToMakeKPeriodic(word = "leetcoleet", k = 2))




