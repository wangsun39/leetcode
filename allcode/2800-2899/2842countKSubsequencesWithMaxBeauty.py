# 给你一个字符串 s 和一个整数 k 。
#
# k 子序列指的是 s 的一个长度为 k 的 子序列 ，且所有字符都是 唯一 的，也就是说每个字符在子序列里只出现过一次。
#
# 定义 f(c) 为字符 c 在 s 中出现的次数。
#
# k 子序列的 美丽值 定义为这个子序列中每一个字符 c 的 f(c) 之 和 。
#
# 比方说，s = "abbbdd" 和 k = 2 ，我们有：
#
# f('a') = 1, f('b') = 3, f('d') = 2
# s 的部分 k 子序列为：
# "abbbdd" -> "ab" ，美丽值为 f('a') + f('b') = 4
# "abbbdd" -> "ad" ，美丽值为 f('a') + f('d') = 3
# "abbbdd" -> "bd" ，美丽值为 f('b') + f('d') = 5
# 请你返回一个整数，表示所有 k 子序列 里面 美丽值 是 最大值 的子序列数目。由于答案可能很大，将结果对 109 + 7 取余后返回。
#
# 一个字符串的子序列指的是从原字符串里面删除一些字符（也可能一个字符也不删除），不改变剩下字符顺序连接得到的新字符串。
#
# 注意：
#
# f(c) 指的是字符 c 在字符串 s 的出现次数，不是在 k 子序列里的出现次数。
# 两个 k 子序列如果有任何一个字符在原字符串中的下标不同，则它们是两个不同的子序列。所以两个不同的 k 子序列可能产生相同的字符串。
#
#
# 示例 1：
#
# 输入：s = "bcca", k = 2
# 输出：4
# 解释：s 中我们有 f('a') = 1 ，f('b') = 1 和 f('c') = 2 。
# s 的 k 子序列为：
# bcca ，美丽值为 f('b') + f('c') = 3
# bcca ，美丽值为 f('b') + f('c') = 3
# bcca ，美丽值为 f('b') + f('a') = 2
# bcca ，美丽值为 f('c') + f('a') = 3
# bcca ，美丽值为 f('c') + f('a') = 3
# 总共有 4 个 k 子序列美丽值为最大值 3 。
# 所以答案为 4 。
# 示例 2：
#
# 输入：s = "abbcd", k = 4
# 输出：2
# 解释：s 中我们有 f('a') = 1 ，f('b') = 2 ，f('c') = 1 和 f('d') = 1 。
# s 的 k 子序列为：
# abbcd ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5
# abbcd ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5
# 总共有 2 个 k 子序列美丽值为最大值 5 。
# 所以答案为 2 。
#
#
# 提示：
#
# 1 <= s.length <= 2 * 105
# 1 <= k <= s.length
# s 只包含小写英文字母。

import math
from leetcode.allcode.competition.mypackage import *

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(s)
        n = len(cnt)
        if n < k: return 0
        l = [[x, c] for x, c in cnt.items()]
        l.sort(key=lambda x: [x[1]], reverse=True)
        mn = l[k - 1][1]  # 与第k项相同的字母都要包含进来
        i = 0
        while i < n and l[i][1] != mn:
            i += 1
        j = i  # 与第k项相同的开始下标
        i += 1
        while i < n and l[i][1] == mn:
            i += 1  # 与第k项相同的结束下标的后一个

        ans = 1
        for x, c in l[:j]:
            ans *= c
            ans %= MOD
        ans *= math.comb(i - j, k - j)  # 从[i, j)中选出k - j 个字母， 每种组合有 l[j][1] ^ k - j个子序列
        ans %= MOD
        ans *= (l[j][1] ** (k - j))

        return ans % MOD

so = Solution()
print(so.countKSubsequencesWithMaxBeauty("dpdemprzvz", 1))  # 1
print(so.countKSubsequencesWithMaxBeauty(s = "fkp", k = 2))  # 3
print(so.countKSubsequencesWithMaxBeauty(s = "abbcd", k = 4))  # 2
print(so.countKSubsequencesWithMaxBeauty(s = "bcca", k = 2))




