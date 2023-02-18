# 给你一个下标从 0 开始的整数数组 nums 。
#
# 现定义两个数字的 串联 是由这两个数值串联起来形成的新数字。
#
# 例如，15 和 49 的串联是 1549 。
# nums 的 串联值 最初等于 0 。执行下述操作直到 nums 变为空：
#
# 如果 nums 中存在不止一个数字，分别选中 nums 中的第一个元素和最后一个元素，将二者串联得到的值加到 nums 的 串联值 上，然后从 nums 中删除第一个和最后一个元素。
# 如果仅存在一个元素，则将该元素的值加到 nums 的串联值上，然后删除这个元素。
# 返回执行完所有操作后 nums 的串联值。
#
#
#
# 示例 1：
#
# 输入：nums = [7,52,2,4]
# 输出：596
# 解释：在执行任一步操作前，nums 为 [7,52,2,4] ，串联值为 0 。
#  - 在第一步操作中：
# 我们选中第一个元素 7 和最后一个元素 4 。
# 二者的串联是 74 ，将其加到串联值上，所以串联值等于 74 。
# 接着我们从 nums 中移除这两个元素，所以 nums 变为 [52,2] 。
#  - 在第二步操作中：
# 我们选中第一个元素 52 和最后一个元素 2 。
# 二者的串联是 522 ，将其加到串联值上，所以串联值等于 596 。
# 接着我们从 nums 中移除这两个元素，所以 nums 变为空。
# 由于串联值等于 596 ，所以答案就是 596 。
# 示例 2：
#
# 输入：nums = [5,14,13,8,12]
# 输出：673
# 解释：在执行任一步操作前，nums 为 [5,14,13,8,12] ，串联值为 0 。
# - 在第一步操作中：
# 我们选中第一个元素 5 和最后一个元素 12 。
# 二者的串联是 512 ，将其加到串联值上，所以串联值等于 512 。
# 接着我们从 nums 中移除这两个元素，所以 nums 变为 [14,13,8] 。
# - 在第二步操作中：
# 我们选中第一个元素 14 和最后一个元素 8 。
# 二者的串联是 148 ，将其加到串联值上，所以串联值等于 660 。
# 接着我们从 nums 中移除这两个元素，所以 nums 变为 [13] 。
# - 在第三步操作中：
# nums 只有一个元素，所以我们选中 13 并将其加到串联值上，所以串联值等于 673 。
# 接着我们从 nums 中移除这个元素，所以 nums 变为空。
# 由于串联值等于 673 ，所以答案就是 673 。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104

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
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
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

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n // 2):
            s1, s2 = str(nums[i]), str(nums[n - 1 - i])
            ans += int(s1 + s2)
        if n & 1:
            ans += int(nums[n // 2])
        return ans


so = Solution()
print(so.findTheArrayConcVal([7,52,2,4]))
print(so.findTheArrayConcVal([5,14,13,8,12]))




