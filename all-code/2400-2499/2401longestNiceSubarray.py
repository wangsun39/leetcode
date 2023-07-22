# 给你一个由 正 整数组成的数组 nums 。
#
# 如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。
#
# 返回 最长 的优雅子数组的长度。
#
# 子数组 是数组中的一个 连续 部分。
#
# 注意：长度为 1 的子数组始终视作优雅子数组。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,3,8,48,10]
# 输出：3
# 解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
# - 3 AND 8 = 0
# - 3 AND 48 = 0
# - 8 AND 48 = 0
# 可以证明不存在更长的优雅子数组，所以返回 3 。
# 示例 2：
#
# 输入：nums = [3,1,5,11,13]
# 输出：1
# 解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109


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
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        cur = nums[i]
        ans = 1
        while j < n:
            if cur & nums[j] == 0:
                cur |= nums[j]
                ans = max(ans, j - i + 1)
                j += 1
            else:
                cur &= ~nums[i]
                i += 1
        return ans


so = Solution()
print(so.longestNiceSubarray([1,3,8,48,10]))
print(so.longestNiceSubarray([3,1,5,11,13]))




