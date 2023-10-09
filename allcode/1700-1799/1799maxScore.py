# 给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。
#
# 在第 i 次操作时（操作编号从 1 开始），你需要：
#
# 选择两个元素 x 和 y 。
# 获得分数 i * gcd(x, y) 。
# 将 x 和 y 从 nums 中删除。
# 请你返回 n 次操作后你能获得的分数和最大为多少。
#
# 函数 gcd(x, y) 是 x 和 y 的最大公约数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2]
# 输出：1
# 解释：最优操作是：
# (1 * gcd(1, 2)) = 1
# 示例 2：
#
# 输入：nums = [3,4,6,8]
# 输出：11
# 解释：最优操作是：
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# 示例 3：
#
# 输入：nums = [1,2,3,4,5,6]
# 输出：14
# 解释：最优操作是：
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
#
#
# 提示：
#
# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 106




from typing import List
import math
from functools import cache
import heapq

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        g = {}
        for i in range(n):
            for j in range(i + 1, n):
                g[(i, j)] = math.gcd(nums[i], nums[j])

        @cache
        def calc(bits, idx):
            if idx * 2 > n:
                return 0
            res = 0
            # print(bin(bits), i)
            for i in range(n):
                if bits & (1 << i) == 0:
                    continue
                for j in range(i + 1, n):
                    if bits & (1 << j) == 0:
                        continue
                    newbits = bits
                    newbits &= (~(1 << i))
                    newbits &= (~(1 << j))
                    res = max(res, g[(i, j)] * idx + calc(newbits, idx + 1))
            return res


        print(g)

        ans = calc(2 ** n - 1, 1)
        return ans



so = Solution()

print(so.maxScore([3,4,6,8]))   # 11
print(so.maxScore([1,2,3,4,5,6]))   # 14
print(so.maxScore([1,2]))   # 1




