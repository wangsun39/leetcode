# 给你一个整数数组 nums 和一个整数 k 。
#
# 找到 nums 中满足以下要求的最长子序列：
#
# 子序列 严格递增
# 子序列中相邻元素的差值 不超过 k 。
# 请你返回满足上述要求的 最长子序列 的长度。
#
# 子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
# 
#  
#
# 示例 1：
#
# 输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
# 输出：5
# 解释：
# 满足要求的最长子序列是 [1,3,4,5,8] 。
# 子序列长度为 5 ，所以我们返回 5 。
# 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
# 示例 2：
#
# 输入：nums = [7,4,5,1,8,12,4,7], k = 5
# 输出：4
# 解释：
# 满足要求的最长子序列是 [4,5,8,12] 。
# 子序列长度为 4 ，所以我们返回 4 。
# 示例 3：
#
# 输入：nums = [1,5], k = 1
# 输出：1
# 解释：
# 满足要求的最长子序列是 [1] 。
# 子序列长度为 1 ，所以我们返回 1 。
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 105

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

class STree:

    def __init__(self):
        self.tree = defaultdict(int)

    def pushup(self, id: int):
        self.tree[id] = max(self.tree[id << 1], self.tree[(id << 1) | 1])

    def update(self, id: int, start: int, end: int, l: int, r: int, val: int):
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[id] = val
            return
        mid = (start + end) >> 1
        self.update(id << 1, start, mid, l, r, val)
        self.update((id << 1) | 1, mid + 1, end, l, r, val)
        self.pushup(id)

    def query(self, id: int, start: int, end: int, l: int, r: int):
        if start > r or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[id]
        mid = (start + end) >> 1
        return max(self.query(id << 1, start, mid, l, r), self.query((id << 1) | 1, mid + 1, end, l, r))

class Solution:


    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        ans = 0
        st = STree()
        for num in nums:
            val = st.query(1, 1, int(1e5), max(1, num - k), num - 1) + 1
            st.update(1, 1, int(1e5), num, num, val)
            ans = max(ans, val)
        return ans


so = Solution()
print(so.lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))
print(so.lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5))
print(so.lengthOfLIS(nums = [1,5], k = 1))




