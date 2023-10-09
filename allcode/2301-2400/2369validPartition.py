# 给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。
#
# 如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
#
# 子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
# 子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
# 子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
# 如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,4,4,5,6]
# 输出：true
# 解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。
# 这是一种有效划分，所以返回 true 。
# 示例 2：
#
# 输入：nums = [1,1,1,2]
# 输出：false
# 解释：该数组不存在有效划分。
#  
#
# 提示：
#
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 106


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

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def helper(idx):
            if idx == n:
                return True
            if idx == n - 1:
                return False
            if idx == n - 2:
                return nums[idx] == nums[idx + 1]
            if idx == n - 3:
                return (nums[idx] == nums[idx + 1] == nums[idx + 2]) or (nums[idx + 2] - nums[idx + 1] == nums[idx + 1] - nums[idx] == 1)
            if nums[idx] == nums[idx + 1] and helper(idx + 2):
                return True
            if nums[idx] == nums[idx + 1] == nums[idx + 2] and helper(idx + 3):
                return True
            if nums[idx + 2] - nums[idx + 1] == nums[idx + 1] - nums[idx] == 1 and helper(idx + 3):
                return True
            return False
        return helper(0)



so = Solution()
print(so.validPartition([4,4,4,5,6]))
print(so.validPartition([1,1,1,2]))




