# 给定一个正整数 n ，你可以做如下操作：
#
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# n 变为 1 所需的最小替换次数是多少？
#
#  
#
# 示例 1：
#
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
# 示例 2：
#
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
# 示例 3：
#
# 输入：n = 4
# 输出：2
#  
#
# 提示：
#
# 1 <= n <= 231 - 1



from typing import List

class Solution:
    def integerReplacement(self, n: int) -> int:
        time = 0
        while n not in (1, 3):
            if n & 1 == 0:
                n >>= 1
            else:
                if (n >> 1) & 1 == 1:
                    n += 1
                else:
                    n -= 1
            time += 1
        if n == 3:
            time += 2
        return time


so = Solution()

print(so.integerReplacement(4))
print(so.integerReplacement(7))
print(so.integerReplacement(8))
print(so.integerReplacement(100000000))

