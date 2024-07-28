

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zero = []
        for i, x in enumerate(s):
            if x == '0':
                zero.append(i)
        m = len(zero)
        ans = 0
        idx = 0  # l 及 l 右侧第一个0在zero中的位置
        for l in range(n):
            while idx < m and l > zero[idx]:
                idx += 1
            for r in range(idx, m):
                if r == l: continue
                n_zero = r - idx
                n_one = r - l - n_zero
                if n_zero ** 2 > n - l:
                    break
                if n_zero ** 2 > n_one:
                    continue
                ans += min(zero[r] - zero[r - 1], n_one - n_zero ** 2)

            n_zero = n - idx
            n_one = n - l - n_zero
            if n_zero ** 2 > n - l:
                ans += min(n - zero[- 1], n_one - n_zero ** 2)
        return ans


so = Solution()
print(so.numberOfSubstrings("00011"))




