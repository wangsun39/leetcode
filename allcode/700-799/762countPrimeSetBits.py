# 给你两个整数left和right ，在闭区间 [left, right]范围内，统计并返回 计算置位位数为质数 的整数个数。
#
# 计算置位位数 就是二进制表示中 1 的个数。
#
# 例如， 21的二进制表示10101有 3 个计算置位。
#
#
# 示例 1：
#
# 输入：left = 6, right = 10
# 输出：4
# 解释：
# 6 -> 110 (2 个计算置位，2 是质数)
# 7 -> 111 (3 个计算置位，3 是质数)
# 9 -> 1001 (2 个计算置位，2 是质数)
# 10-> 1010 (2 个计算置位，2 是质数)
# 共计 4 个计算置位为质数的数字。
# 示例 2：
#
# 输入：left = 10, right = 15
# 输出：5
# 解释：
# 10 -> 1010 (2 个计算置位, 2 是质数)
# 11 -> 1011 (3 个计算置位, 3 是质数)
# 12 -> 1100 (2 个计算置位, 2 是质数)
# 13 -> 1101 (3 个计算置位, 3 是质数)
# 14 -> 1110 (3 个计算置位, 3 是质数)
# 15 -> 1111 (4 个计算置位, 4 不是质数)
# 共计 5 个计算置位为质数的数字。
#
#
# 提示：
#
# 1 <= left <= right <= 106
# 0 <= right - left <= 104


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        def count(n):
            ans = 0
            while n > 0:
                n = n & (n - 1)
                ans += 1
            return ans
        res = 0
        for i in range(left, right + 1):
            ans = count(i)
            if ans in primes:
                res += 1
        return res


so = Solution()
print(so.countPrimeSetBits(6, 10))
print(so.countPrimeSetBits(10, 15))

