# 给你两个长度都为 n 的字符串 s 和 t 。你可以对字符串 s 执行以下操作：
#
# 将 s 长度为 l （0 < l < n）的 后缀字符串 删除，并将它添加在 s 的开头。
# 比方说，s = 'abcd' ，那么一次操作中，你可以删除后缀 'cd' ，并将它添加到 s 的开头，得到 s = 'cdab' 。
# 给你一个整数 k ，请你返回 恰好 k 次操作将 s 变为 t 的方案数。
#
# 由于答案可能很大，返回答案对 109 + 7 取余 后的结果。
#
#
#
# 示例 1：
#
# 输入：s = "abcd", t = "cdab", k = 2
# 输出：2
# 解释：
# 第一种方案：
# 第一次操作，选择 index = 3 开始的后缀，得到 s = "dabc" 。
# 第二次操作，选择 index = 3 开始的后缀，得到 s = "cdab" 。
#
# 第二种方案：
# 第一次操作，选择 index = 1 开始的后缀，得到 s = "bcda" 。
# 第二次操作，选择 index = 1 开始的后缀，得到 s = "cdab" 。
# 示例 2：
#
# 输入：s = "ababab", t = "ababab", k = 1
# 输出：2
# 解释：
# 第一种方案：
# 选择 index = 2 开始的后缀，得到 s = "ababab" 。
#
# 第二种方案：
# 选择 index = 4 开始的后缀，得到 s = "ababab" 。
#
#
# 提示：
#
# 2 <= s.length <= 5 * 105
# 1 <= k <= 1015
# s.length == t.length
# s 和 t 都只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

import numpy as np

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10 ** 9 + 7

        def kmp(text: str, pattern: str) -> List[int]:
            # 在文本串 text 中查找模式串 pattern，返回所有成功匹配的位置（pattern[0] 在 text 中的下标）
            m = len(pattern)
            pi = [0] * m  # 前缀子串 s[:i + 1] 的真前缀和真后缀的最长匹配
            c = 0
            for i in range(1, m):
                v = pattern[i]
                while c and pattern[c] != v:
                    c = pi[c - 1]
                if pattern[c] == v:
                    c += 1
                pi[i] = c

            res = []
            c = 0
            for i, v in enumerate(text):
                v = text[i]
                while c and pattern[c] != v:
                    c = pi[c - 1]
                if pattern[c] == v:
                    c += 1
                if c == len(pattern):
                    res.append(i - m + 1)
                    c = pi[c - 1]
            return res

        def pow(matrix, n):  # (mat ^ n) % MOD  矩阵快速幂
            res = np.eye(2, dtype=object)
            cur = matrix.copy()
            while n:
                if n & 1:
                    res = np.matmul(cur, res)
                    res %= MOD
                cur = np.matmul(cur, cur)
                cur %= MOD
                n >>= 1
            return res

        s2 = s * 2
        idx = kmp(s2[:-1], t)
        c = len(idx)
        n = len(s)
        if s == t:
            x0 = np.array([1, 0])  # 初始向量
        else:
            x0 = np.array([0, 1])

        A = np.array([[c - 1, c],
                      [n - c, n - c - 1]])

        A = pow(A, k)
        xk = np.matmul(A, x0)
        return xk[0]


so = Solution()
print(so.numberOfWays(s = "abcd", t = "cdab", k = 2))




