# 给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
#
# i < j < k ，
# nums[j] - nums[i] == diff 且
# nums[k] - nums[j] == diff
# 返回不同 算术三元组 的数目。
#
# 
#
# 示例 1：
#
# 输入：nums = [0,1,4,6,7,10], diff = 3
# 输出：2
# 解释：
# (1, 2, 4) 是算术三元组：7 - 4 == 3 且 4 - 1 == 3 。
# (2, 4, 5) 是算术三元组：10 - 7 == 3 且 7 - 4 == 3 。
# 示例 2：
#
# 输入：nums = [4,5,6,7,8,9], diff = 2
# 输出：2
# 解释：
# (0, 2, 4) 是算术三元组：8 - 6 == 2 且 6 - 4 == 2 。
# (1, 3, 5) 是算术三元组：9 - 7 == 2 且 7 - 5 == 2 。
# 
#
# 提示：
#
# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums 严格 递增

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
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        ans = 0
        for i, e in enumerate(nums):
            if e + diff in s and e + diff * 2 in s:
                ans += 1
        return ans


so = Solution()
print(so.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print(so.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))




