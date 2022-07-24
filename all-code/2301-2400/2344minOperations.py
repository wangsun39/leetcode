# 给你两个正整数数组 nums 和 numsDivide 。你可以从 nums 中删除任意数目的元素。
#
# 请你返回使 nums 中 最小 元素可以整除 numsDivide 中所有元素的 最少 删除次数。如果无法得到这样的元素，返回 -1 。
#
# 如果 y % x == 0 ，那么我们说整数 x 整除 y 。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
# 输出：2
# 解释：
# [2,3,2,4,3] 中最小元素是 2 ，它无法整除 numsDivide 中所有元素。
# 我们从 nums 中删除 2 个大小为 2 的元素，得到 nums = [3,4,3] 。
# [3,4,3] 中最小元素为 3 ，它可以整除 numsDivide 中所有元素。
# 可以证明 2 是最少删除次数。
# 示例 2：
#
# 输入：nums = [4,3,6], numsDivide = [8,2,6,10]
# 输出：-1
# 解释：
# 我们想 nums 中的最小元素可以整除 numsDivide 中的所有元素。
# 没有任何办法可以达到这一目的。
#  
#
# 提示：
#
# 1 <= nums.length, numsDivide.length <= 105
# 1 <= nums[i], numsDivide[i] <= 109

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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
import math
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gys = numsDivide[0]
        for e in numsDivide[1:]:
            gys = math.gcd(gys, e)
        nums.sort()
        for i, e in enumerate(nums):
            if gys % e == 0:
                return i
        return -1




so = Solution()
print(so.minOperations(nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]))
print(so.minOperations(nums = [4,3,6], numsDivide = [8,2,6,10]))




