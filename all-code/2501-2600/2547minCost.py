# 给你一个整数数组 nums 和一个整数 k 。
#
# 将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。
#
# 令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。
#
# 例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
# 子数组的 重要性 定义为 k + trimmed(subarray).length 。
#
# 例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
# 找出并返回拆分 nums 的所有可行方案中的最小代价。
#
# 子数组 是数组的一个连续 非空 元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2,1,3,3], k = 2
# 输出：8
# 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
# [1,2] 的重要性是 2 + (0) = 2 。
# [1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
# 拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
# 示例 2：
#
# 输入：nums = [1,2,1,2,1], k = 2
# 输出：6
# 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
# [1,2] 的重要性是 2 + (0) = 2 。
# [1,2,1] 的重要性是 2 + (2) = 4 。
# 拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
# 示例 3：
#
# 输入：nums = [1,2,1,2,1], k = 5
# 输出：10
# 解释：将 nums 拆分成一个子数组：[1,2,1,2,1].
# [1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
# 拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# 1 <= k <= 109

from typing import List
from typing import Optional
from cmath import inf
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
from math import *
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
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
from heapq import *
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	表示这个数的二进制表示中最低位的1所对应的值
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
    # SortedList.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
    # SortedList.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
    # SortedList.clear() 移除所有元素。时间复杂度O(n).
    # SortedList.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
    # SortedList.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
    # SortedList.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
    # SortedList.bisect_left(value)
    # SortedList.bisect_right(value)
    # SortedList.count(value)
    # SortedList.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        len_trim = [[0] * n for _ in range(n)]
        for i in range(n):
            counter = Counter()
            counter[nums[i]] = 1
            for j in range(i + 1, n):
                len_trim[i][j] = len_trim[i][j - 1]
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    len_trim[i][j] += 2
                elif counter[nums[j]] > 2:
                    len_trim[i][j] += 1
        # print(len_trim)
        @cache
        def dfs(i, j):   # [i, j)
            if i + 1 > j: return 0
            res = inf
            for t in range(i, j):  # [i, t]  (t, j)
                res = min(res, k + len_trim[i][t] + dfs(t + 1, j))
            # print(i, j, res)
            return res
        return dfs(0, n)


so = Solution()
print(so.minCost(nums = [1,2,1,2,1], k = 5))
print(so.minCost(nums = [1,2,1], k = 2))
print(so.minCost(nums = [1,2,1,2,1], k = 2))
print(so.minCost(nums = [1,2,1,2,1,3,3], k = 2))




