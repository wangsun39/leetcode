# 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。
#
# 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。
#
# 如果以下条件满足，我们称这些塔是 美丽 的：
#
# 1 <= heights[i] <= maxHeights[i]
# heights 是一个 山状 数组。
# 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山状 数组：
#
# 对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
# 对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
# 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。
#
#
#
# 示例 1：
#
# 输入：maxHeights = [5,3,4,1,1]
# 输出：13
# 解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山状数组，峰值在 i = 0 处。
# 13 是所有美丽塔方案中的最大高度和。
# 示例 2：
#
# 输入：maxHeights = [6,5,3,9,2,7]
# 输出：22
# 解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山状数组，峰值在 i = 3 处。
# 22 是所有美丽塔方案中的最大高度和。
# 示例 3：
#
# 输入：maxHeights = [3,2,5,5,2,3]
# 输出：18
# 解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山状数组，最大值在 i = 2 处。
# 注意，在这个方案中，i = 3 也是一个峰值。
# 18 是所有美丽塔方案中的最大高度和。
#
#
# 提示：
#
# 1 <= n == maxHeights <= 105
# 1 <= maxHeights[i] <= 109

from typing import List
from typing import Optional
from cmath import *
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise, accumulate
# list(accumulate(nums))  数组前缀和
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# print(c.most_common(2)) # n = 2
#  [('c', 3), ('b', 2)]

# d = defaultdict(int)
# from math import *
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword
# a.isalpha()  # 判断字符串中是否所有的字符都是字母
# a.isdigit() # 判断字符串中是否所有的字符都是整数
# a.isalnum()  # 判断字符串中是否所有的字符都是字母or数字
# a.isspace()  # 判断字符串中是否所有的字符都是空白符
# a.swapcase()  # 转换大小写

from bisect import *
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# k = bisect_left(a, x) - 1 # k 表示 < x 的最大下标， 不存在: k == -1
# k = bisect_right(a, x) - 1 # k 表示 <= x 的最大下标， 不存在: k == -1
# k = bisect_right(a, x) # k 表示 > x 的最小下标， 不存在: k == n
# k = bisect_left(a, x)  # k 表示 >= x 的最小下标， 不存在: k == n

# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
from heapq import *
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数  这2个性能很差

# Map = [['U' for _ in range(n)] for _ in range(m)]
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List, Tuple
# @lru_cache(None)

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串  ascii_lowercase[x] 当0<=x<26可以得到一个字符
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串
# c2i = {c: i for i, c in enumerate(ascii_lowercase)}

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList, SortedDict, SortedSet
# sl = SortedList()
# sl.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
# sl.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
# sl.clear() 移除所有元素。时间复杂度O(n).
# sl.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
# sl.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
# sl.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
# sl.bisect_left(value)
# sl.bisect_right(value)
# sl.count(value)
# sl.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

# sd = SortedDict({'a': 1, 'b': 2, 'c': 3})
# skv = sd.keys()  这个是有序的

# ss = SortedSet()
# ss.add(value)
# ss.pop()
# ss.pop(value)
# ss.remove(value)
# ss.remove(value)


# 前缀和
# 左闭右开区间 [left,right) 来表示从 nums[left] 到 nums[right−1] 的子数组，
# 此时子数组的和为 s[right]−s[left]，子数组的长度为 right−left。
# s = list(accumulate(nums, initial=0))

# dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
# list(zip(nums))  # [([7, 2, 1],), ([6, 4, 2],), ([6, 5, 3],), ([3, 2, 1],)]   合并
# list(zip(*nums))  # [(7, 6, 6, 3), (2, 4, 5, 2), (1, 2, 3, 1)]    转置

class Solution:
    def maximumSumOfHeights1(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left, stack, right = [-1] * n, [], [-1] * n

        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        dp1 = [0] * n
        for i, x in enumerate(maxHeights):
            if i == 0:
                dp1[i] = maxHeights[0]
                continue
            if maxHeights[i - 1] <= x:
                dp1[i] = dp1[i - 1] + x
            else:
                if left[i] == -1:
                    dp1[i] = x * (i + 1)
                else:
                    dp1[i] = dp1[left[i]] + x * (i - left[i])
        dp2 = [0] * n
        for i in range(n - 1, -1, -1):
            x = maxHeights[i]
            if i == n - 1:
                dp2[i] = x
                continue
            if x >= maxHeights[i + 1]:
                dp2[i] = dp2[i + 1] + x
            else:
                if right[i] == -1:
                    dp2[i] = x * (n - i)
                else:
                    dp2[i] = dp2[right[i]] + x * (right[i] - i)
        ans = 0
        for i in range(n):
            ans = max(ans, dp1[i] + dp2[i] - maxHeights[i])
        return ans

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        # 2023/12/21 单调栈重写
        n = len(maxHeights)

        def proc(l):  # 返回一个列表ll,其中ll[i]表示以l[i]为最高点，左侧之和的最大值
            res = [0] * n
            stack = []  # stack[i] = [a,b,c] a表示高度，b表示被a顶掉的多少项,c表示a的下标
            for i, x in enumerate(l):
                cnt = 0
                while stack and stack[-1][0] > x:
                    a, b, c = stack.pop()
                    cnt += (b + 1)
                res[i] = cnt * x
                if stack:
                    res[i] += (res[stack[-1][2]] + stack[-1][0])
                stack.append([x, cnt, i])
            return res
        left = proc(maxHeights)
        right = proc(maxHeights[::-1])[::-1]
        ans = -inf
        for i in range(n):
            cur = maxHeights[i] + left[i] + right[i]
            ans = max(ans, cur)
        return ans

so = Solution()




