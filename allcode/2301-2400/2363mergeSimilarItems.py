# 给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质：
#
# items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。
# items 中每件物品的价值都是 唯一的 。
# 请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。
#
# 注意：ret 应该按价值 升序 排序后返回。
#
#
#
# 示例 1：
#
# 输入：items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# 输出：[[1,6],[3,9],[4,5]]
# 解释：
# value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 5 ，总重量为 1 + 5 = 6 。
# value = 3 的物品再 items1 中 weight = 8 ，在 items2 中 weight = 1 ，总重量为 8 + 1 = 9 。
# value = 4 的物品在 items1 中 weight = 5 ，总重量为 5 。
# 所以，我们返回 [[1,6],[3,9],[4,5]] 。
# 示例 2：
#
# 输入：items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
# 输出：[[1,4],[2,4],[3,4]]
# 解释：
# value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 3 ，总重量为 1 + 3 = 4 。
# value = 2 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 1 ，总重量为 3 + 1 = 4 。
# value = 3 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
# 所以，我们返回 [[1,4],[2,4],[3,4]] 。
# 示例 3：
#
# 输入：items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
# 输出：[[1,7],[2,4],[7,1]]
# 解释：
# value = 1 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 4 ，总重量为 3 + 4 = 7 。
# value = 2 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
# value = 7 的物品在 items2 中 weight = 1 ，总重量为 1 。
# 所以，我们返回 [[1,7],[2,4],[7,1]] 。
#
#
# 提示：
#
# 1 <= items1.length, items2.length <= 1000
# items1[i].length == items2[i].length == 2
# 1 <= valuei, weighti <= 1000
# items1 中每个 valuei 都是 唯一的 。
# items2 中每个 valuei 都是 唯一的 。


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

import time
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dd = defaultdict(int)
        for k, v in items1 + items2:
            dd[k] += v
        return sorted([[k, v] for k, v in dd.items()])




so = Solution()




