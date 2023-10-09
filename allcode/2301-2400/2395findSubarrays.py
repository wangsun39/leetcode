# 给你一个下标从 0 开始的整数数组 nums ，判断是否存在 两个 长度为 2 的子数组且它们的 和 相等。注意，这两个子数组起始位置的下标必须 不相同 。
#
# 如果这样的子数组存在，请返回 true，否则返回 false 。
#
# 子数组 是一个数组中一段连续非空的元素组成的序列。
#
#
#
# 示例 1：
#
# 输入：nums = [4,2,4]
# 输出：true
# 解释：元素为 [4,2] 和 [2,4] 的子数组有相同的和 6 。
# 示例 2：
#
# 输入：nums = [1,2,3,4,5]
# 输出：false
# 解释：没有长度为 2 的两个子数组和相等。
# 示例 3：
#
# 输入：nums = [0,0,0]
# 输出：true
# 解释：子数组 [nums[0],nums[1]] 和 [nums[1],nums[2]] 的和相等，都为 0 。
# 注意即使子数组的元素相同，这两个子数组也视为不相同的子数组，因为它们在原数组中的起始位置不同。
#
#
# 提示：
#
# 2 <= nums.length <= 1000
# -109 <= nums[i] <= 109


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
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        c = Counter()
        for i in range(0, n - 1):
            c[nums[i] + nums[i + 1]] += 1
        return any(v >= 2 for v in c.values())


so = Solution()
print(so.findSubarrays([4,2,4]))
print(so.findSubarrays([0,0,0]))
print(so.findSubarrays([1,2,3,4,5]))




