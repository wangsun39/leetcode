
from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
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
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sub1 = [nums1[i] - nums2[i] for i in range(n)]
        sub2 = [nums2[i] - nums1[i] for i in range(n)]
        def maxArray(arr):
            dp = [0] * n
            dp[0] = arr[0]
            ans = dp[0]
            for i in range(1, n):
                dp[i] = max(arr[i], dp[i - 1] + arr[i])
                ans = max(ans, dp[i])
            return ans
        r1, r2 = maxArray(sub1), maxArray(sub2)
        # print(r1,r2)
        return max(sum(nums1) + r2, sum(nums2) + r1)

so = Solution()
print(so.maximumsSplicedArray(nums1 = [60,160,60], nums2 = [10,90,10]))
print(so.maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10]))
print(so.maximumsSplicedArray([20,40,20,70,30], nums2 = [50,20,50,40,20]))
print(so.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1]))




