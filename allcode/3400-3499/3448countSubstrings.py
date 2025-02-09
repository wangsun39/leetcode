

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubstrings(self, s: str) -> int:
        s = [int(x) for x in s]
        n = len(s)

        def proc(k):
            dp = [[0] * k for _ in range(n)]  # dp[i][j] 以s[i]结尾的子串，mod k 余数为j的子串个数
            dp[0][s[0] % k] = 1
            for i in range(1, n):
                dp[i][s[i] % k] += 1
                for j in range(k):
                    v = (j * 10 + s[i]) % k
                    dp[i][v] += dp[i - 1][j]
            return dp

        dp2 = proc(2)
        dp3 = proc(3)
        dp4 = proc(4)
        dp7 = proc(7)
        dp9 = proc(9)

        ans = 1 if s[0] else 0
        for i in range(1, n):
            if s[i] == 0: continue
            if s[i] in {1, 2, 5}: ans += i + 1
            elif s[i] == 3: ans += dp3[i - 1][0] + 1
            elif s[i] == 4: ans += dp2[i - 1][0] + 1
            elif s[i] == 6: ans += dp3[i - 1][0] + 1
            elif s[i] == 7: ans += dp7[i - 1][0] + 1
            elif s[i] == 8: ans += dp4[i - 1][0] + 1
            elif s[i] == 9: ans += dp9[i - 1][0] + 1
            # print(i, ans)
        return ans


so = Solution()
print(so.countSubstrings(s = "12936"))
print(so.countSubstrings(s = "5701283"))




