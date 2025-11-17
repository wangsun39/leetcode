# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
#
# 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1：
#
# 输入："3+2*2"
# 输出：7
# 示例 2：
#
# 输入：" 3/2 "
# 输出：1
# 示例 3：
#
# 输入：" 3+5 / 2 "
# 输出：5
# 说明：
#
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def calculate(self, s: str) -> int:
        q1 = []
        left = 0
        for right, x in enumerate(s):
            if x in '+-':
                q1.append(s[left: right])
                q1.append(x)
                left = right + 1
        q1.append(s[left:])

        def calc(ss):
            q = []
            l = 0
            for i, x in enumerate(ss):
                if x in '*/':
                    q.append(int(ss[l: i]))
                    q.append(x)
                    l = i + 1
            q.append(int(ss[l:]))
            ans = q[0]
            for i in range(1, len(q), 2):
                if q[i] == '*':
                    ans *= q[i + 1]
                else:
                    ans //= q[i + 1]
            return ans
        for i in range(0, len(q1), 2):
            q1[i] = calc(q1[i])
        ans = q1[0]
        for i in range(1, len(q1), 2):
            if q1[i] == '+':
                ans += q1[i + 1]
            else:
                ans -= q1[i + 1]
        return ans


so = Solution()
print(so.calculate("3+2*2"))




