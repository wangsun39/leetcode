# 给你一个下标从 0 开始、长度为 n 的二进制字符串 s ，你可以对其执行两种操作：
#
# 选中一个下标 i 并且反转从下标 0 到下标 i（包括下标 0 和下标 i ）的所有字符，成本为 i + 1 。
# 选中一个下标 i 并且反转从下标 i 到下标 n - 1（包括下标 i 和下标 n - 1 ）的所有字符，成本为 n - i 。
# 返回使字符串内所有字符 相等 需要的 最小成本 。
#
# 反转 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。
#
#
#
# 示例 1：
#
# 输入：s = "0011"
# 输出：2
# 解释：执行第二种操作，选中下标 i = 2 ，可以得到 s = "0000" ，成本为 2 。可以证明 2 是使所有字符相等的最小成本。
# 示例 2：
#
# 输入：s = "010101"
# 输出：9
# 解释：执行第一种操作，选中下标 i = 2 ，可以得到 s = "101101" ，成本为 3 。
# 执行第一种操作，选中下标 i = 1 ，可以得到 s = "011101" ，成本为 2 。
# 执行第一种操作，选中下标 i = 0 ，可以得到 s = "111101" ，成本为 1 。
# 执行第二种操作，选中下标 i = 4 ，可以得到 s = "111110" ，成本为 2 。
# 执行第一种操作，选中下标 i = 5 ，可以得到 s = "111111" ，成本为 1 。
# 使所有字符相等的总成本等于 9 。可以证明 9 是使所有字符相等的最小成本。
#
#
# 提示：
#
# 1 <= s.length == n <= 105
# s[i] 为 '0' 或 '1'
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumCost(self, s: str) -> int:
        seg = []
        start = 0
        n = len(s)
        for i, x in enumerate(s[1:], 1):
            if x == s[start]:
                continue
            seg.append(i - start)
            start = i
        seg.append(n - start)
        print(seg)
        m = len(seg)
        def func(sg):
            ll = [0] * m
            # acc = sg[0]  # 前缀和
            # ll[0] = sg[0]
            acc = 0  # 前缀和
            ll[0] = 0
            for i in range(m - 1):
                acc += sg[i]
                ll[i + 1] = ll[i] + acc
            return ll

        l, r = func(seg), func(seg[::-1])[::-1]
        print(l, r)
        ans = inf
        for i in range(m):
            ans = min(ans, l[i] + r[i])
        return ans



so = Solution()
print(so.minimumCost("0011"))
print(so.minimumCost("010101"))




