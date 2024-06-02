

from leetcode.allcode.competition.mypackage import *

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        # i2c = {i: c for i, c in enumerate(ascii_lowercase)}
        delFlg = [0] * n
        idx = [[] for _ in range(26)]

        for i, x in enumerate(s):
            if x != '*':
                idx[c2i[x]].append(i)
                continue
            for j in range(26):
                if len(idx[j]) > 0:
                    k = idx[j].pop()
                    delFlg[k] = 1
                    break
        ans = []
        for i, x in enumerate(s):
            if x == '*' or delFlg[i]: continue
            ans.append(x)
        return ''.join(ans)




so = Solution()
print(so.clearStars("d*"))
print(so.clearStars("aaba*"))
print(so.clearStars("abc"))




