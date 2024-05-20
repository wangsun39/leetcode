# 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
#
# 「超赞子字符串」需满足满足下述两个条件：
#
# 该字符串是 s 的一个非空子字符串
# 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
#
#
# 示例 1：
#
# 输入：s = "3242415"
# 输出：5
# 解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
# 示例 2：
#
# 输入：s = "12345678"
# 输出：1
# 示例 3：
#
# 输入：s = "213123"
# 输出：6
# 解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
# 示例 4：
#
# 输入：s = "00"
# 输出：2
#
#
# 提示：
#
# 1 <= s.length <= 10^5
# s 仅由数字组成

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestAwesome(self, s: str) -> int:
        s = list(s)
        s = [int(x) for x in s]
        d = {0: -1}  # 记录某种奇偶组合出现的最早下标，用10个bit的二进制数，分别表示0-9的个数的奇偶性，0是偶数，1是奇数
        cur = 0
        ans = 0
        for i, x in enumerate(s):
            # 把cur的第i位的奇偶性兑换，也就是做取反操作
            cur ^= (1 << x)
            if cur in d:
                ans = max(ans, i - d[cur])
            else:
                d[cur] = i
            for j in range(10):
                v = cur ^ (1 << j)
                if v in d:
                    ans = max(ans, i - d[v])
        return ans

so = Solution()
print(so.longestAwesome("12345678"))
print(so.longestAwesome("3242415"))
print(so.longestAwesome("213123"))
print(so.longestAwesome("00"))

