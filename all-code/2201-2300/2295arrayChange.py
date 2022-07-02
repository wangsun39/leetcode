# 给你一个下标从 0 开始的数组 nums ，它包含 n 个 互不相同 的正整数。请你对这个数组执行 m 个操作，在第 i 个操作中，你需要将数字 operations[i][0] 替换成 operations[i][1] 。
#
# 题目保证在第 i 个操作中：
#
# operations[i][0] 在 nums 中存在。
# operations[i][1] 在 nums 中不存在。
# 请你返回执行完所有操作后的数组。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
# 输出：[3,2,7,1]
# 解释：我们对 nums 执行以下操作：
# - 将数字 1 替换为 3 。nums 变为 [3,2,4,6] 。
# - 将数字 4 替换为 7 。nums 变为 [3,2,7,6] 。
# - 将数字 6 替换为 1 。nums 变为 [3,2,7,1] 。
# 返回最终数组 [3,2,7,1] 。
# 示例 2：
#
# 输入：nums = [1,2], operations = [[1,3],[2,1],[3,2]]
# 输出：[2,1]
# 解释：我们对 nums 执行以下操作：
# - 将数字 1 替换为 3 。nums 变为 [3,2] 。
# - 将数字 2 替换为 1 。nums 变为 [3,1] 。
# - 将数字 3 替换为 2 。nums 变为 [2,1] 。
# 返回最终数组 [2,1] 。
#
#
# 提示：
#
# n == nums.length
# m == operations.length
# 1 <= n, m <= 105
# nums 中所有数字 互不相同 。
# operations[i].length == 2
# 1 <= nums[i], operations[i][0], operations[i][1] <= 106
# 在执行第 i 个操作时，operations[i][0] 在 nums 中存在。
# 在执行第 i 个操作时，operations[i][1] 在 nums 中不存在。

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

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idx = {}
        for i, e in enumerate(nums):
            idx[e] = i
        for oper in operations:
            pos = idx[oper[0]]
            nums[pos] = oper[1]
            del idx[oper[0]]
            idx[oper[1]] = pos
        return nums



so = Solution()
print(so.arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]))
print(so.arrayChange(nums = [1,2], operations = [[1,3],[2,1],[3,2]]))
print(so.arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]))




