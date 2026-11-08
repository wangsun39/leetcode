# 给你一个由正整数组成的整数数组 nums 和一个整数 k。

# 一个 子数组 的 质因数集合 是其所有元素的 不同质 因数的 并集。

# 返回 最长子数组的长度 ，其质因数集合中包含的不同质因子数量不超过 k 。如果不存在这样的子数组，则返回 0。

# 子数组 是数组中一段连续 非空 的元素序列。

# 质数 是指在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数的自然数。

#

# 示例 1：

# 输入： nums = [7,6,10,12,11], k = 3

# 输出： 3

# 解释：

# 子数组 [6, 10, 12]：

# 6 的不同质因数是 {2, 3}。
# 10 的不同质因数是 {2, 5}。
# 12 的不同质因数是 {2, 3}。
# 这些集合的并集是 {2, 3, 5}，包含 3 个不同质因数。
# 没有更长的子数组满足条件。因此，答案是 3。

# 示例 2：

# 输入： nums = [4,6,9,18], k = 4

# 输出： 4

# 解释：

# 整个数组 [4, 6, 9, 18]：

# 4 的不同质因数是 {2}。
# 6 的不同质因数是 {2, 3}。
# 9 的不同质因数是 {3}。
# 18 的不同质因数是 {2, 3}。
# 这些集合的并集是 {2, 3}，包含 2 个不同质因数。
# 因为 2 <= 4，所以整个数组是有效的。因此，答案是 4。

# 示例 3：

# 输入： nums = [6,10,15], k = 2

# 输出： 1

# 解释：

# 所有长度至少为 2 的子数组的质因数集合均为 {2, 3, 5}，包含 3 个不同质因数。

# 因为 3 > 2，只有长度为 1 的子数组是有效的。因此，答案是 1。

#

# 提示：

# 1 <= nums.length <= 105
# 2 <= nums[i] <= 105
# 1 <= k <= 104

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

MX = 10 ** 5 + 1
# MX = 10 

factors = []  # factors[i][j] 表示i的质因子j的个数
factors.append(None)
factors.append(defaultdict(int))

for x in range(2, MX):
    factors.append(defaultdict(int))
    y = 2
    while y * y <= x:
        while x % y == 0:
            factors[-1][y] += 1
            x //= y
        y += 1
    if x > 1:
        factors[-1][x] += 1  # 剩余的一个质数


# print(factors)

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        r = 0
        counter = Counter()

        def check():
            return len(counter) <= k

        def put(x):
            for y in factors[x].keys():
                counter[y] += 1

        def pop(x):
            for y in factors[x].keys():
                counter[y] -= 1
                if counter[y] == 0:
                    del (counter[y])

        ans = 0
        for l in range(n):
            while check() and r < n:
                put(nums[r])
                r += 1
                if len(counter) > k:
                    break
                else:
                    ans = max(ans, r - l)

            pop(nums[l])
        return ans


so = Solution()
print(so.longestSubarray(nums = [7,6,10,12,11], k = 3))



