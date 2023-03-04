# 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
#
# 按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
#
# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
#
# 示例 1：
#
# 输入：nums = [2,1,3]
# 输出：12
# 解释：可以选出如下 i, j, k 三元组：
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
# 示例 2：
#
# 输入：nums = [0,0,0]
# 输出：27
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 216

from collections import Counter
from typing import List

class Solution:
    def countTriplets1(self, nums: List[int]) -> int:
        counter = Counter()  # counter[i]  记录与 i 做 & 运算为 0 的元素的个数
        for i in range(2 ** 16):
            for x in nums:
                if x & i == 0:
                    counter[i] += 1

        ans = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i:], i):
                if i != j:
                    ans += counter[x & y] * 2
                else:
                    ans += counter[x]
        return ans

    def countTriplets(self, nums: List[int]) -> int:
        counter = Counter()  # counter[i]  记录 i 的个数
        for x in nums:
            for y in nums:
                counter[x & y] += 1
        ans = 0
        for x in nums:
            for k, v in counter.items():
                if x & k == 0:
                    ans += v
        return ans




so = Solution()
print(so.countTriplets([2,1,3]))
print(so.countTriplets([0,0,0]))

