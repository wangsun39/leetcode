# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
#
# 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
#
# 返回使 s 单调递增的最小翻转次数。
#
#  
#
# 示例 1：
#
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
# 示例 2：
#
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
# 示例 3：
#
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。
#  
#
# 提示：
#
# 1 <= s.length <= 105
# s[i] 为 '0' 或 '1'

from collections import Counter
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        counter = Counter(s)
        ans, cur = counter['1'], counter['1']
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                cur -= 1
                ans = min(ans, cur)
            else:
                cur += 1
        return ans


so = Solution()
print(so.minFlipsMonoIncr('00110'))
print(so.minFlipsMonoIncr('010110'))
print(so.minFlipsMonoIncr('00011000'))