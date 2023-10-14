

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        sd = set(dictionary)
        n = len(s)

        @cache
        def dfs(idx):
            if idx == n:
                return 0
            res = inf
            for j in range(idx, n):
                if s[idx: j + 1] in sd:
                    res = min(res, dfs(j + 1))
                else:
                    if j - idx + 1 < res:
                        res = min(res, j - idx + 1 + dfs(j + 1))
            # print(idx, res)
            return res
        return dfs(0)




so = Solution()
print(so.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
print(so.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))




