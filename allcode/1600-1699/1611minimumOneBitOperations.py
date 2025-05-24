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
        # 2 ^ n 变成 0 需要 2 ^ (n+1) - 1 次
        def f(x: int):  # 将 x 变成 0的操作次数
            # 先将 x 变成只剩二进制最高位一个 1的数字z，再把z变成0
            if x <= 1: return x
            if x.bit_count() == 1:
                return x * 2 - 1
            # 将 x 的次高位变成1，后面都是0的形式 y
            # x => z + y => y => 0
            # x => z + y 相当于 x - z => y: g(x - z, y)
            # z + y => y 需要一次
            # y => 0 需要 y * 2 - 1 次
            l = x.bit_length()  # 获取z的二进制长度
            y = 1 << (l - 2)
            z = 1 << (l - 1)
            return g(x - z, y) + y * 2

        def g(x, y):  # 将 x 变成 y 的操作次数，y的二进制之多只有一个1
            if x == y: return 0
            if x & y:
                # x 中 y的这一个bit位已经是1了，只需要把其他位变成0即可
                return f(x ^ y)
            # x 中 y 的这一个bit位不是1了，就要先将其变成1
            # 那就需要先将其后面变成1000...的形式，设为z
            # x => z => y + z => y
            # z => y + z 要 1 步
            # y + z => y 要 z * 2 - 1 == y - 1 步
            z = y >> 1
            return g(x, z) + y

        return f(n)


so = Solution()
print(so.minimumOneBitOperations(9))   # 14
print(so.minimumOneBitOperations(3))
print(so.minimumOneBitOperations(2))
print(so.minimumOneBitOperations(6))


