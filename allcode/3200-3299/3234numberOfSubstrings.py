

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zero = []
        for i, x in enumerate(s):
            if x == '0':
                zero.append(i)
        if len(zero) == 0:
            return n * (n + 1) // 2
        zero.append(n)
        m = len(zero)
        ans = 0
        idx = 0 if zero[0] > 0 else 1  # l 右侧第一个0在zero中的位置
        for l in range(n):
            if l >= zero[idx]:
                idx += 1
            for r in range(idx, m):
                n_zero = r - idx  # [l, zero[r]) 有多少个0
                if s[l] == '0': n_zero += 1
                n_one = zero[r] - l - n_zero  # [l, zero[r]) 有多少个1
                if n_zero ** 2 > n - l - n_zero:  # [l, zero[r]) 中 0 的个数平方超过 [l, n) 中1的个数的上限
                    break
                if n_zero ** 2 > n_one:
                    continue
                if r > 0:
                    ans += min(zero[r] - max(l, zero[r - 1]), n_one - n_zero ** 2 + 1)
                else:
                    ans += min(zero[r] - l, n_one - n_zero ** 2 + 1)

        return ans


so = Solution()
print(so.numberOfSubstrings("101101"))  # 16
print(so.numberOfSubstrings("1"))  # 16
print(so.numberOfSubstrings("00011"))  # 5




