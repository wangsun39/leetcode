# 给定一个二进制字符串 s 和两个整数 num1 和 num2。num1 和 num2 为互质。
#
# 比率子串 是 s 的子串，其中子串中 0 的数量与 1 的数量之比正好是 num1 : num2。
#
# 例如，如果 num1 = 2 和 num2 = 3，那么 "01011" 和 "1110000111" 是比率子串，而 "11000" 不是。
# 返回 s 的 非空 比率子串的个数。
#
# 注意:
#
# 子串 是字符串中连续的字符序列。
# 如果 gcd(x, y) == 1，则 x 和 y 为 互质，其中 gcd(x, y) 为 x 和 y 的最大公约数。
#
#
# 示例 1:
#
# 输入: s = "0110011", num1 = 1, num2 = 2
# 输出: 4
# 解释: 有 4 个非空的比率子串。
# - 子字符串 s[0..2]: "0110011"。它包含一个 0 和两个 1。比例是 1:2。
# - 子字符串 s[1..4]: "0110011"。它包含一个 0 和两个 1。比例是 1:2。
# - 子字符串 s[4..6]: "0110011"。它包含一个 0 和两个 1。比例是 1:2。
# - 子字符串 s[1..6]: "0110011"。它包含两个 0 和四个 1。比例是 2:4 == 1:2。
# 它可以显示没有更多的比率子串。
# 示例 2:
#
# 输入: s = "10101", num1 = 3, num2 = 1
# 输出: 0
# 解释: s 没有比率子串，返回 0。
#
#
# 提示:
#
# 1 <= s.length <= 105
# 1 <= num1, num2 <= s.length
# num1 和 num2 互质。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        # num1 / num2 == (presum0[i] - presum0[j]) / (presum1[i] - presum1[j])
        # num1 * presum1[j] - num2 * presum0[j] == num1 * presum1[i] - num2 * presum0[i]
        s0 = s1 = 0
        counter = Counter()
        counter[0] = 1  # 边界
        ans = 0
        for i, x in enumerate(s):
            if x == '0':
                s0 += 1
            else:
                s1 += 1
            ans += counter[num1 * s1 - num2 * s0]
            counter[num1 * s1 - num2 * s0] += 1
        return ans



so = Solution()
print(so.fixedRatio(s = "0110011", num1 = 1, num2 = 2))
print(so.fixedRatio(s = "10101", num1 = 3, num2 = 1))




