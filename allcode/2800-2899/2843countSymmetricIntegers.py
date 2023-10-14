# 给你两个正整数 low 和 high 。
#
# 对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。
#
# 返回在 [low, high] 范围内的 对称整数的数目 。
#
#
#
# 示例 1：
#
# 输入：low = 1, high = 100
# 输出：9
# 解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
# 示例 2：
#
# 输入：low = 1200, high = 1230
# 输出：4
# 解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
#
#
# 提示：
#
# 1 <= low <= high <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def cnt(x):
            s = list(str(x))
            s = [int(x) for x in s]
            n = len(s)
            if n & 1: return 0
            if sum(s[: n // 2]) == sum(s[n // 2:]):
                return 1
            return 0
        ans = 0
        for i in range(low, high + 1):
            ans += cnt(i)
        return ans


so = Solution()
print(so.countSymmetricIntegers(low = 1, high = 100))
print(so.countSymmetricIntegers(low = 1200, high = 1230))




