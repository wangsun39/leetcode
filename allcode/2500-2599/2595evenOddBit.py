# 给你一个 正 整数 n 。
#
# 用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。
#
# 用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。
#
# 返回整数数组 answer ，其中 answer = [even, odd] 。
#
#
#
# 示例 1：
#
# 输入：n = 17
# 输出：[2,0]
# 解释：17 的二进制形式是 10001 。
# 下标 0 和 下标 4 对应的值为 1 。
# 共有 2 个偶数下标，0 个奇数下标。
# 示例 2：
#
# 输入：n = 2
# 输出：[0,1]
# 解释：2 的二进制形式是 10 。
# 下标 1 对应的值为 1 。
# 共有 0 个偶数下标，1 个奇数下标。
#
#
# 提示：
#
# 1 <= n <= 1000

from leetcode.allcode.competition.mypackage import *


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)[2:]
        # print(b)
        n = len(b)
        x = y = 0
        for i in range(n):
            if i & 1:
                if b[n - 1 - i] == '1':
                    y += 1
            else:
                if b[n - 1 - i] == '1':
                    x += 1
        return [x, y]




so = Solution()
print(so.evenOddBit(17))
print(so.evenOddBit(2))




