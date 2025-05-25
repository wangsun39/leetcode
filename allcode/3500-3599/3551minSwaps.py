# 给你一个由 互不相同 的正整数组成的数组 nums，需要根据每个数字的数位和（即每一位数字相加求和）按 升序 对数组进行排序。如果两个数字的数位和相等，则较小的数字排在前面。
#
# 返回将 nums 排列为上述排序顺序所需的 最小 交换次数。
#
# 一次 交换 定义为交换数组中两个不同位置的值。
#
#
#
# 示例 1：
#
# 输入: nums = [37,100]
#
# 输出: 1
#
# 解释:
#
# 计算每个整数的数位和：[3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
# 根据数位和排序：[100, 37]。将 37 与 100 交换，得到排序后的数组。
# 因此，将 nums 排列为排序顺序所需的最小交换次数为 1。
# 示例 2：
#
# 输入: nums = [22,14,33,7]
#
# 输出: 0
#
# 解释:
#
# 计算每个整数的数位和：[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
# 根据数位和排序：[22, 14, 33, 7]。数组已经是排序好的。
# 因此，将 nums 排列为排序顺序所需的最小交换次数为 0。
# 示例 3：
#
# 输入: nums = [18,43,34,16]
#
# 输出: 2
#
# 解释:
#
# 计算每个整数的数位和：[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
# 根据数位和排序：[16, 34, 43, 18]。将 18 与 16 交换，再将 43 与 34 交换，得到排序后的数组。
# 因此，将 nums 排列为排序顺序所需的最小交换次数为 2。
#
#
# 提示:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# nums 由 互不相同 的正整数组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        bits = [[0] * 2 for _ in range(n)]
        for i, x in enumerate(nums):
            y = x
            res = 0
            while x:
                res += x % 10
                x //= 10
            bits[i] = [res, y, i]
        bits.sort()

        fa = list(range(n))

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        for i, [_, _, j] in enumerate(bits):
            union(i, j)

        for i in range(n):
            find(i)
        counter = Counter(fa)
        ans = 0
        for x in counter.values():
            ans += x - 1
        return ans


so = Solution()
print(so.minSwaps([18,43,34,16]))




