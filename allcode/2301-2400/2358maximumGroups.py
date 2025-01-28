# 给你一个正整数数组 grades ，表示大学中一些学生的成绩。你打算将 所有 学生分为一些 有序 的非空分组，其中分组间的顺序满足以下全部条件：
#
# 第 i 个分组中的学生总成绩 小于 第 (i + 1) 个分组中的学生总成绩，对所有组均成立（除了最后一组）。
# 第 i 个分组中的学生总数 小于 第 (i + 1) 个分组中的学生总数，对所有组均成立（除了最后一组）。
# 返回可以形成的 最大 组数。
#
# 
#
# 示例 1：
#
# 输入：grades = [10,6,12,7,3,5]
# 输出：3
# 解释：下面是形成 3 个分组的一种可行方法：
# - 第 1 个分组的学生成绩为 grades = [12] ，总成绩：12 ，学生数：1
# - 第 2 个分组的学生成绩为 grades = [6,7] ，总成绩：6 + 7 = 13 ，学生数：2
# - 第 3 个分组的学生成绩为 grades = [10,3,5] ，总成绩：10 + 3 + 5 = 18 ，学生数：3
# 可以证明无法形成超过 3 个分组。
# 示例 2：
#
# 输入：grades = [8,8]
# 输出：1
# 解释：只能形成 1 个分组，因为如果要形成 2 个分组的话，会导致每个分组中的学生数目相等。
# 
#
# 提示：
#
# 1 <= grades.length <= 105
# 1 <= grades[i] <= 105


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
import math

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        ans = int((math.sqrt(8 * n + 1) - 1)) // 2
        return ans


so = Solution()
print(so.maximumGroups([10,6,12,7,3,5]))
print(so.maximumGroups([8, 8]))




