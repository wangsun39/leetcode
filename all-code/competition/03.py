# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度均为 n 。
#
# 让我们定义另一个下标从 0 开始、长度为 n 的整数数组，nums3 。对于范围 [0, n - 1] 的每个下标 i ，你可以将 nums1[i] 或 nums2[i] 的值赋给 nums3[i] 。
#
# 你的任务是使用最优策略为 nums3 赋值，以最大化 nums3 中 最长非递减子数组 的长度。
#
# 以整数形式表示并返回 nums3 中 最长非递减 子数组的长度。
#
# 注意：子数组 是数组中的一个连续非空元素序列。
#
#
#
# 示例 1：
#
# 输入：nums1 = [2,3,1], nums2 = [1,2,1]
# 输出：2
# 解释：构造 nums3 的方法之一是：
# nums3 = [nums1[0], nums2[1], nums2[2]] => [2,2,1]
# 从下标 0 开始到下标 1 结束，形成了一个长度为 2 的非递减子数组 [2,2] 。
# 可以证明 2 是可达到的最大长度。
# 示例 2：
#
# 输入：nums1 = [1,3,2,1], nums2 = [2,2,3,4]
# 输出：4
# 解释：构造 nums3 的方法之一是：
# nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] => [1,2,3,4]
# 整个数组形成了一个长度为 4 的非递减子数组，并且是可达到的最大长度。
# 示例 3：
#
# 输入：nums1 = [1,1], nums2 = [2,2]
# 输出：2
# 解释：构造 nums3 的方法之一是：
# nums3 = [nums1[0], nums1[1]] => [1,1]
# 整个数组形成了一个长度为 2 的非递减子数组，并且是可达到的最大长度。
#
#
# 提示：
#
# 1 <= nums1.length == nums2.length == n <= 105
# 1 <= nums1[i], nums2[i] <= 109

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
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List, Tuple
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
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

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
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1, dp2 = [1] * n, [1] * n # 以nums1[i]结尾的最长子数组长度
        # dp1[0] = dp2[0] = 1
        ans = 1
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = max(dp1[i], dp1[i - 1] + 1)
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = max(dp2[i], dp2[i - 1] + 1)
            ans = max(dp1[i], dp2[i], ans)
        # print(dp1, dp2)
        return ans



so = Solution()
print(so.maxNonDecreasingLength([8,7,4], [13,4,4]))
print(so.maxNonDecreasingLength(nums1 = [2,3,1], nums2 = [1,2,1]))
print(so.maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4]))
print(so.maxNonDecreasingLength(nums1 = [1,1], nums2 = [2,2]))




