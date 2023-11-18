

from leetcode.allcode.competition.mypackage import *

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 4: return 0
        dp2 = [0] * 12  # 枚举12种可能。递推
        dp1 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 23]
        for i in range(1, n):
            dp2[11] = dp1[11] * 23   #  不包含任何l/e/t
            dp2[0] = dp1[0] * 24 + dp1[11]  # 仅包含 'l' 至少1个
            dp2[1] = dp1[1] * 23 + dp1[11]  # 仅包含 'e' 1个
            dp2[2] = dp1[2] * 24 + dp1[11]  # 仅包含 't' 至少1个
            dp2[3] = dp1[0] + dp1[1] + dp1[3] * 24  # 仅包含 'le'
            dp2[4] = dp1[1] + dp1[2] + dp1[4] * 24  # 仅包含 'te'
            dp2[5] = dp1[1] + dp1[5] * 24  # 仅包含 'e' 至少2个
            dp2[6] = dp1[0] + dp1[2] + dp1[6] * 25  # 仅包含 'lt'
            dp2[7] = dp1[3] + dp1[4] + dp1[6] + dp1[7] * 25  # 仅包含 'let'
            dp2[8] = dp1[3] + dp1[5] + dp1[8] * 25  # 仅包含 'lee'
            dp2[9] = dp1[4] + dp1[5] + dp1[9] * 25  # 仅包含 'tee'
            dp2[10] = dp1[7] + dp1[8] + dp1[9] + dp1[10] * 26  # 包含 'leet'
            for j in range(12):
                dp2[j] %= MOD
            dp1, dp2 = dp2, [0] * 12
        return dp1[-2]




so = Solution()
print(so.stringCount(5))
print(so.stringCount(4))
print(so.stringCount(10))




