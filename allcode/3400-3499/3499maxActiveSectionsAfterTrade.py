

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        intv = []
        cnt1 = s.count('1')
        s = '01' + s + '10'
        for i, x in enumerate(s[1:], 1):
            if x != s[i - 1]:
                intv.append(i)
        if len(intv) == 4:   # 原始串为 0011 或 11100，不能有任何操作
            return cnt1
        if len(intv) <= 6:   # 可以使得操作之和全为 1
            return len(s) - 4
        ans = 0  # 能将最多的0变成1的个数
        for i in range(0, len(intv) - 5, 2):
            ans = max(ans, intv[i + 4] - intv[i + 3] + intv[i + 2] - intv[i + 1])  # 将两个挨着的全0区间都变成1
        return ans + cnt1


so = Solution()
print(so.maxActiveSectionsAfterTrade("10100101"))
print(so.maxActiveSectionsAfterTrade("0100"))
print(so.maxActiveSectionsAfterTrade("01101001"))
print(so.maxActiveSectionsAfterTrade("01"))




