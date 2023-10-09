# 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标 removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
#
# 一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
#
# 请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
#
# 注意：一个下标至多只会被删除一次。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
# 输出：[14,7,2,2,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。
# 查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。
# 查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。
# 查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。
# 查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [14,7,2,2,0] 。
# 示例 2：
#
# 输入：nums = [3,2,11,1], removeQueries = [3,2,1,0]
# 输出：[16,5,3,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。
# 查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。
# 查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。
# 查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [16,5,3,0] 。
#  
#
# 提示：
#
# n == nums.length == removeQueries.length
# 1 <= n <= 105
# 1 <= nums[i] <= 109
# 0 <= removeQueries[i] < n
# removeQueries 中所有数字 互不相同 。
#
# https://leetcode.cn/problems/maximum-segment-sum-after-removals
from itertools import accumulate
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

from sortedcontainers import SortedList
class Solution:
    def maximumSegmentSum1(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        fa = list(range(n))  # 存放每个点所在连通块的代表元（未必每个点的fa值都是最新的，调用find获取，不要直接fa[i]获取）
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        sumOf = [0] * n  # 存放每个点所属连通块内元素之和
        ans = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            sumOf[x] = nums[x]
            if x < n - 1:
                if sumOf[x + 1]:
                    sumOf[x] += sumOf[x + 1]
                    fa[x + 1] = x
            if x > 0:
                y = find(x - 1)
                if sumOf[y] > 0:
                    sumOf[y] += sumOf[x]
                    fa[x] = y
            ans[i - 1] = max(ans[i], sumOf[fa[x]])
        return ans

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        # 2023/9/19  有序数组，性能不如上面的
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        sl1 = SortedList([s[-1]])  # 剩余的区间和排序数组
        sl2 = SortedList([[0, n - 1]])  # 剩余的区间排序数组
        ans = []
        for x in removeQueries:
            if len(sl2) == 0:
                ans.append(0)
                continue
            p = sl2.bisect_left([x, n])
            a, b = sl2[p - 1]
            lp = s[b + 1] - s[a]
            sl2.pop(p - 1)
            sl1.remove(lp)
            if x - a >= 1:
                sl1.add(s[x] - s[a])
                sl2.add([a, x - 1])
            if b - x >= 1:
                sl1.add(s[b + 1] - s[x + 1])
                sl2.add([x + 1, b])
            if len(sl1):
                ans.append(sl1[-1])
            else:
                ans.append(0)
        return ans





so = Solution()
print(so.maximumSegmentSum(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]))  # [14,7,2,2,0]
print(so.maximumSegmentSum(nums = [500,822,202,707,298,484,311,680,901,319,343,340], removeQueries = [6,4,0,5,2,3,10,8,7,9,1,11]))  # [3013,2583,2583,2583,2583,2583,1900,822,822,822,340,0]
print(so.maximumSegmentSum(nums = [3,2,11,1], removeQueries = [3,2,1,0]))  # [16,5,3,0]




