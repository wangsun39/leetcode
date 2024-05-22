# 给你一个长度为 n 下标从 0 开始的数组 nums ，数组中所有数字均为非负整数。对于 0 到 n - 1 之间的每一个下标 i ，你需要找出 nums 中一个 最小 非空子数组，它的起始位置为 i （包含这个位置），同时有 最大 的 按位或运算值 。
#
# 换言之，令 Bij 表示子数组 nums[i...j] 的按位或运算的结果，你需要找到一个起始位置为 i 的最小子数组，这个子数组的按位或运算的结果等于 max(Bik) ，其中 i <= k <= n - 1 。
# 一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。
#
# 请你返回一个大小为 n 的整数数组 answer，其中 answer[i]是开始位置为 i ，按位或运算结果最大，且 最短 子数组的长度。
#
# 子数组 是数组里一段连续非空元素组成的序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,2,1,3]
# 输出：[3,3,2,2,1]
# 解释：
# 任何位置开始，最大按位或运算的结果都是 3 。
# - 下标 0 处，能得到结果 3 的最短子数组是 [1,0,2] 。
# - 下标 1 处，能得到结果 3 的最短子数组是 [0,2,1] 。
# - 下标 2 处，能得到结果 3 的最短子数组是 [2,1] 。
# - 下标 3 处，能得到结果 3 的最短子数组是 [1,3] 。
# - 下标 4 处，能得到结果 3 的最短子数组是 [3] 。
# 所以我们返回 [3,3,2,2,1] 。
# 示例 2：
#
# 输入：nums = [1,2]
# 输出：[2,1]
# 解释：
# 下标 0 处，能得到最大按位或运算值的最短子数组长度为 2 。
# 下标 1 处，能得到最大按位或运算值的最短子数组长度为 1 。
# 所以我们返回 [2,1] 。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] <= 109

from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = [-1] * 32  # 第 i 个bit位是1的最小下标
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            x = nums[i]
            for j in range(32):
                if (x >> j) & 1:
                    pos[j] = i
            ans[i] = max(max(pos) - i + 1, 1)  # 至少是1
        return ans


so = Solution()
print(so.smallestSubarrays([0]))
print(so.smallestSubarrays([1,0,2,1,3]))



