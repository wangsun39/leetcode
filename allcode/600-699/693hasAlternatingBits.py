# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
#
#
#
# 示例 1：
#
# 输入：n = 5
# 输出：true
# 解释：5 的二进制表示是：101
# 示例 2：
#
# 输入：n = 7
# 输出：false
# 解释：7 的二进制表示是：111.
# 示例 3：
#
# 输入：n = 11
# 输出：false
# 解释：11 的二进制表示是：1011.
#
#
# 提示：
#
# 1 <= n <= 231 - 1


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        n >>= 1
        while n > 0:
            cur = n & 1
            if not cur ^ last:
                return False
            last = cur
            n >>= 1
        return True


so = Solution()
print(so.hasAlternatingBits(5))
print(so.hasAlternatingBits(7))
print(so.hasAlternatingBits(11))
