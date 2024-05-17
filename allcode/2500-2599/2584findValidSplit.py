# 给你一个长度为 n 的整数数组 nums ，下标从 0 开始。
#
# 如果在下标 i 处 分割 数组，其中 0 <= i <= n - 2 ，使前 i + 1 个元素的乘积和剩余元素的乘积互质，则认为该分割 有效 。
#
# 例如，如果 nums = [2, 3, 3] ，那么在下标 i = 0 处的分割有效，因为 2 和 9 互质，而在下标 i = 1 处的分割无效，因为 6 和 3 不互质。在下标 i = 2 处的分割也无效，因为 i == n - 1 。
# 返回可以有效分割数组的最小下标 i ，如果不存在有效分割，则返回 -1 。
#
# 当且仅当 gcd(val1, val2) == 1 成立时，val1 和 val2 这两个值才是互质的，其中 gcd(val1, val2) 表示 val1 和 val2 的最大公约数。
#
#
#
# 示例 1：
#
#
#
# 输入：nums = [4,7,8,15,3,5]
# 输出：2
# 解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
# 唯一一个有效分割位于下标 2 。
# 示例 2：
#
#
#
# 输入：nums = [4,7,15,8,3,5]
# 输出：-1
# 解释：上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
# 不存在有效分割。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 104
# 1 <= nums[i] <= 106
from math import gcd

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findValidSplit1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return -1
        if n == 2:
            return 0 if gcd(nums[0], nums[1]) == 1 else -1
        left = 0
        right = n - 1
        ans = 0
        while left + 1 < right:
            while gcd(nums[left], nums[right]) == 1 and ans < right:
                right -= 1
            if left == ans == right:
                return ans
            ans = right
            left += 1
            right = n - 1
        return -1 if left < ans else ans


    def findValidSplit(self, nums: List[int]) -> int:
        # 2024/5/17 质因子分解
        def prime_factors(x):
            res = []
            i = 2
            while i * i <= x:
                if x % i != 0:
                    i += 1
                    continue
                res.append(i)
                while x % i == 0:
                    x //= i
                i += 1
            if x > 1:
                res.append(x)
            return res
        n = len(nums)
        if n == 1: return -1
        mid = 0
        for i in range(n):
            x = nums[i]
            p = prime_factors(x)
            for y in p:
                for j in range(i + 1, n):
                    if nums[j] % y == 0:
                        mid = max(mid, j)
                        if mid == n - 1:
                            return -1
                        while nums[j] % y == 0:
                            nums[j] //= y
            if mid == i:
                return mid



so = Solution()
print(so.findValidSplit([4,7,8,15,3,5]))  # 2
print(so.findValidSplit([4,7,15,8,3,5]))  # -1




