# 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
#
# 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
#
# 如果存在这样的分法，请返回 True ；否则，返回 False 。
#
#
#
# 示例 1：
#
# 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
# 示例 2：
#
# 输入：arr = [1,2,3,4,5,6], k = 7
# 输出：true
# 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
# 示例 3：
#
# 输入：arr = [1,2,3,4,5,6], k = 10
# 输出：false
# 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
#
#
# 提示：
#
# arr.length == n
# 1 <= n <= 105
# n 为偶数
# -109 <= arr[i] <= 109
# 1 <= k <= 105

from heapq import *
from collections import defaultdict, Counter
from functools import cache
from typing import List
from math import *

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [x % k for x in arr]
        counter = Counter(arr)
        for kk, v in counter.items():
            if kk == 0: continue
            if v != counter[k - kk]: return False
            if kk * 2 == k and v & 1: return False
        return True



so = Solution()
print(so.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
print(so.canArrange(arr = [1,2,3,4,5,6], k = 7))
print(so.canArrange(arr = [1,2,3,4,5,6], k = 10))




