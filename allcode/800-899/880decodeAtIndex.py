# 给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：
#
# 如果所读的字符是字母，则将该字母写在磁带上。
# 如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
# 现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。
#
#
#
# 示例 1：
#
# 输入：S = "leet2code3", K = 10
# 输出："o"
# 解释：
# 解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
# 字符串中的第 10 个字母是 "o"。
# 示例 2：
#
# 输入：S = "ha22", K = 5
# 输出："h"
# 解释：
# 解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
# 示例 3：
#
# 输入：S = "a2345678999999999999999", K = 1
# 输出："a"
# 解释：
# 解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
#
#
# 提示：
#
# 2 <= S.length <= 100
# S 只包含小写字母与数字 2 到 9 。
# S 以字母开头。
# 1 <= K <= 10^9
# 题目保证 K 小于或等于解码字符串的长度。
# 解码后的字符串保证少于 2^63 个字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def decodeAtIndex(self, S: str, k: int) -> str:
        loop = []  # loop[i] == [l, s, n]  表示前面的长度为l的字符串，接一个字符串s，一共翻n倍，前长度为l的字符串在loop下一项中表示
        curs = ''
        curl = 0
        for x in S:
            if x.isalpha():
                curs += x
            else:
                x = int(x)
                loop.insert(0, [curl, curs, x])
                curl = (curl + len(curs)) * x
                curs = ''
        if len(loop) == 0:
            return S[k - 1]

        for l, s, n in loop:
            single = l + len(s)  # 单个周期长度
            pos = (k - 1) % single
            k %= single
            if pos >= l:
                return s[pos - l]





so = Solution()
print(so.decodeAtIndex(S = "abc", k = 1))
print(so.decodeAtIndex(S = "a2345678999999999999999", k = 1))
print(so.decodeAtIndex(S = "leet2code3", k = 10))
print(so.decodeAtIndex(S = "ha22", k = 5))




