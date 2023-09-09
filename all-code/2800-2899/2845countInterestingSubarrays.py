# 给你一个下标从 0 开始的整数数组 nums ，以及整数 modulo 和整数 k 。
#
# 请你找出并统计数组中 趣味子数组 的数目。
#
# 如果 子数组 nums[l..r] 满足下述条件，则称其为 趣味子数组 ：
#
# 在范围 [l, r] 内，设 cnt 为满足 nums[i] % modulo == k 的索引 i 的数量。并且 cnt % modulo == k 。
# 以整数形式表示并返回趣味子数组的数目。
#
# 注意：子数组是数组中的一个连续非空的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,4], modulo = 2, k = 1
# 输出：3
# 解释：在这个示例中，趣味子数组分别是：
# 子数组 nums[0..0] ，也就是 [3] 。
# - 在范围 [0, 0] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
# - 因此 cnt = 1 ，且 cnt % modulo == k 。
# 子数组 nums[0..1] ，也就是 [3,2] 。
# - 在范围 [0, 1] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
# - 因此 cnt = 1 ，且 cnt % modulo == k 。
# 子数组 nums[0..2] ，也就是 [3,2,4] 。
# - 在范围 [0, 2] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。
# - 因此 cnt = 1 ，且 cnt % modulo == k 。
# 可以证明不存在其他趣味子数组。因此，答案为 3 。
# 示例 2：
#
# 输入：nums = [3,1,9,6], modulo = 3, k = 0
# 输出：2
# 解释：在这个示例中，趣味子数组分别是：
# 子数组 nums[0..3] ，也就是 [3,1,9,6] 。
# - 在范围 [0, 3] 内，只存在 3 个下标 i = 0, 2, 3 满足 nums[i] % modulo == k 。
# - 因此 cnt = 3 ，且 cnt % modulo == k 。
# 子数组 nums[1..1] ，也就是 [1] 。
# - 在范围 [1, 1] 内，不存在下标满足 nums[i] % modulo == k 。
# - 因此 cnt = 0 ，且 cnt % modulo == k 。
# 可以证明不存在其他趣味子数组，因此答案为 2 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= modulo <= 109
# 0 <= k < modulo

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
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        nums = [int(x % modulo == k) for x in nums]
        counter = Counter()  # counter[i]  模 module 余 i 的个数
        counter[0] = 1
        s = 0  # 前缀和
        ans = 0
        for x in nums:  # 遍历子数组右端点，计算有多少个左端点
            s += x
            n1 = s % modulo  # x为右端点的模数
            if n1 >= k:
                n2 = n1 - k   # 左端点左侧需要的模数
            else:
                n2 = modulo + n1 - k
            ans += counter[n2]
            counter[n1] += 1

        return ans




so = Solution()
print(so.countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1))
print(so.countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0))
print(so.countInterestingSubarrays(nums = [11,12,21,31], modulo = 10, k = 1))




