# 给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ：
#
# 翻转 n 的二进制表示中最右侧位（第 0 位）。
# 如果第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。
# 返回将 n 转换为 0 的最小操作次数。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：2
# 解释：3 的二进制表示为 "11"
# "11" -> "01" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "01" -> "00" ，执行的是第 1 种操作。
# 示例 2：
#
# 输入：n = 6
# 输出：4
# 解释：6 的二进制表示为 "110".
# "110" -> "010" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
# "010" -> "011" ，执行的是第 1 种操作。
# "011" -> "001" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "001" -> "000" ，执行的是第 1 种操作。
#
#
# 提示：
#
# 0 <= n <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bi = list(bin(n)[2:])
        m = len(bi)
        ans = 0
        for i in range(m):
            if bi[m - 1 - i] == '1':
                ans += (1 + i + 1) * (i + 1) // 2
                if m - 1 - i > 0 and bi[m - i - 2] == '1':
                    bi[m - i - 2] = '0'
                    ans += 1
        return ans

so = Solution()
print(so.minimumOneBitOperations(9))
print(so.minimumOneBitOperations(3))
print(so.minimumOneBitOperations(6))


