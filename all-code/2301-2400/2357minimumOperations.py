# 给你一个非负整数数组 nums 。在一步操作中，你必须：
#
# 选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
# nums 中的每个正整数都减去 x。
# 返回使 nums 中所有元素都等于 0 需要的 最少 操作数。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,5,0,3,5]
# 输出：3
# 解释：
# 第一步操作：选出 x = 1 ，之后 nums = [0,4,0,2,4] 。
# 第二步操作：选出 x = 2 ，之后 nums = [0,2,0,0,2] 。
# 第三步操作：选出 x = 2 ，之后 nums = [0,0,0,0,0] 。
# 示例 2：
#
# 输入：nums = [0]
# 输出：0
# 解释：nums 中的每个元素都已经是 0 ，所以不需要执行任何操作。
#  
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
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
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if counter[0] > 0:
            return len(counter.keys()) - 1
        return len(counter.keys())


so = Solution()
print(so.minimumOperations([1,5,0,3,5]))
print(so.minimumOperations([0]))




