
from leetcode.allcode.competition.mypackage import *


class Solution:
    # z[i] 表示 s 和 s[i:]的最长公共前缀
    def z_function(s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        z[0] = n   # 这里根据实际考虑是否为n
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z


