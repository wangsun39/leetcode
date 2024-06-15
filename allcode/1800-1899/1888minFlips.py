# 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：
#
# 类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
# 类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
# 请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。
#
# 我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。
#
# 比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
#
#
# 示例 1：
#
# 输入：s = "111000"
# 输出：2
# 解释：执行第一种操作两次，得到 s = "100011" 。
# 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
# 示例 2：
#
# 输入：s = "010"
# 输出：0
# 解释：字符串已经是交替的。
# 示例 3：
#
# 输入：s = "1110"
# 输出：1
# 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
#
#
# 提示：
#
# 1 <= s.length <= 105
# s[i] 要么是 '0' ，要么是 '1' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0

        def f(ss):  # 将ss转成0101...的形式，需要最少的第二种操作次数
            m = 0  # 不做第一种操作，只做第二种操作次数
            for i, x in enumerate(ss):
                if (i & 1 and x == '0') or (i & 1 == 0 and x == '1'):
                    m += 1
            if m == 0 or n & 1 == 0:  # 长度为偶数，答案就是m
                return m
            x1 = 0
            res = m
            for i, x in enumerate(ss):
                if (i & 1 and x == '0') or (i & 1 == 0 and x == '1'):
                    x1 += 1  # s[:i + 1] 需要执行第二种操作次数
                x2 = m - x1  # s[i + 1:] 需要执行第二种操作次数
                n1 = i + 1  # s[:i + 1] 长度
                n2 = n - n1  # s[i + 1:] 长度
                # s[:i + 1] 和 s[i + 1:] 对调，可能的第二种操作次数有两种
                res = min(res, x2 + n1 - x1, x1 + n2 - x2)
            return res
        s2 = list(s)  # 把s的0和1互相调换，这样函数f只需要考虑，转成0101...的形式
        s2 = ['0' if x == '1' else '1' for x in s2]
        s2 = ''.join(s2)
        return min(f(s), f(s2))

    def minFlips(self, s: str) -> int:
        # 2024/6/15  换个写法
        n = len(s)
        # n1 表示转成1010...的操作次数，n2 表示转成0101...的操作次数
        # 有关系n1 + n2 == n
        n1 = sum(1 for i, x in enumerate(s) if (i & 1 == 0 and x == '0' or i & 1 == 1 and x == '1'))
        n2 = n - n1
        if n & 1 == 0: # 长度为偶数
            return min(n1, n2)
        ans = min(n1, n2)
        for i in range(1, n):
            # n1, n2 = n2 + int(s[i - 1] == '1'), n1 + int(s[i - 1] == '0')
            if s[i - 1] == '0':
                n1 = n2 + 1
            else:
                n1 = n2 - 1
            n2 = n - n1
            ans = min(ans, min(n1, n2))
        return ans



so = Solution()
print(so.minFlips(s = "10100101011001111110"))
print(so.minFlips(s = "01001001101"))
print(so.minFlips(s = "001000000010"))
print(so.minFlips(s = "010"))
print(so.minFlips(s = "111000"))
print(so.minFlips(s = "1110"))




