# 给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。
#
# 对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：
#
# 下标 i 之前 的 k 个元素是 非递增的 。
# 下标 i 之后 的 k 个元素是 非递减的 。
# 按 升序 返回所有好下标。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,1,1,1,3,4,1], k = 2
# 输出：[2,3]
# 解释：数组中有两个好下标：
# - 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
# - 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
# 注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
# 示例 2：
#
# 输入：nums = [2,1,1,2], k = 2
# 输出：[]
# 解释：数组中没有好下标。
#  
#
# 提示：
#
# n == nums.length
# 3 <= n <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= n / 2
#
# https://leetcode.cn/problems/find-all-good-indices

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
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
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
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        nums1 = []
        n = len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 0:
                nums1.append(0)
            elif nums[i] - nums[i - 1] > 0:
                nums1.append(1)
            elif nums[i] - nums[i - 1] < 0:
                nums1.append(-1)
        print(nums1)
        stack1 = [-1]
        cur = -1
        for i in range(n - 1):
            stack1.append(cur)
            if nums1[i] == 1:
                cur = i + 1
        print(stack1)
        stack2 = [10000000]
        cur = 10000000
        for i in range(n - 2, -1, -1):
            stack2.insert(0, cur)
            if nums1[i] == -1:
                cur = i
        print(stack2)
        ans = []
        for i in range(k, n - k):
            if i - stack1[i] >= k and stack2[i] - i >= k:
                ans.append(i)
        return ans


so = Solution()
print(so.goodIndices(nums = [877464,394689,51354,348332,285490,570624], k = 2))
print(so.goodIndices(nums = [2,1,1,1,3,4,1], k = 2))
print(so.goodIndices(nums = [2,1,1,2], k = 2))




