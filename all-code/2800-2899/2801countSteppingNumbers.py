# 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
#
# 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
#
# 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
#
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
# 注意：步进数字不能有前导 0 。
#
#
#
# 示例 1：
#
# 输入：low = "1", high = "11"
# 输出：10
# 解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。
# 示例 2：
#
# 输入：low = "90", high = "101"
# 输出：2
# 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
#
#
# 提示：
#
# 1 <= int(low) <= int(high) < 10100
# 1 <= low.length, high.length <= 100
# low 和 high 只包含数字。
# low 和 high 都不含前导 0 。

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
    def countSteppingNumbers1(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7

        def f(s: str):  # 数字 <= num 满足条件的所有数字
            n = len(s)
            @cache
            def helper(i: int, is_limit: bool, pre: int) -> int:
                if i == len(s):
                    return 1
                ans = 0
                can = []
                if pre > 0:
                    if not is_limit or int(s[i]) >= pre - 1:
                        can.append(pre - 1)
                if pre < 9 and (not is_limit or int(s[i]) >= pre + 1):
                    can.append(pre + 1)
                for j in can:
                    if not is_limit:
                        ans += helper(i + 1, is_limit, j)
                    else:
                        if j == int(s[i]):
                            ans += helper(i + 1, is_limit, j)
                        else:
                            ans += helper(i + 1, False, j)
                    ans %= MOD
                return ans
            ans = 0
            # 长度为n的数
            for i in range(1, int(s[0]) + 1):
                if i < int(s[0]):
                    ans += helper(1, False, i)
                else:
                    ans += helper(1, True, i)
                ans %= MOD

            @cache
            def helper2(i: int, pre: int, ll) -> int:
                if i == ll:
                    return 1
                ans = 0
                can = []
                if pre > 0:
                    can.append(pre - 1)
                if pre < 9:
                    can.append(pre + 1)
                for j in can:
                    ans += helper2(i + 1, j, ll)
                    ans %= MOD
                return ans
            for length in range(1, n):
                for i in range(1, 10):
                    ans += helper2(1, i, length)
                    ans %= MOD

            return ans

        low = str(int(low) - 1)
        # print(f(high))
        # print(f(low))
        return (f(high) + MOD - f(low)) % MOD
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7

        def f(s: str):  # 数字 <= num 满足条件的所有数字
            @cache
            def helper(i: int, is_limit: bool, pre: int, is_num: bool) -> int:
                if i == len(s):
                    return is_num
                ans = 0
                if not is_num:
                    ans = helper(i + 1, False, -1, False)

                if pre == -1:
                    if is_limit:
                        can = list(range(1, int(s[i]) + 1))
                    else:
                        can = list(range(1, 10))
                else:
                    can = []
                    if pre > 0:
                        can.append(pre - 1)
                    if pre < 9:
                        can.append(pre + 1)
                    if is_limit:
                        can = [x for x in can if x <= int(s[i])]

                for j in can:
                    if not is_limit:
                        ans += helper(i + 1, False, j, True)
                    else:
                        if j == int(s[i]):
                            ans += helper(i + 1, True, j, True)
                        else:
                            ans += helper(i + 1, False, j, True)
                    ans %= MOD
                return ans
            return helper(0, True, -1, False)

        low = str(int(low) - 1)
        # print(f(high))
        # print(f(low))
        return (f(high) + MOD - f(low)) % MOD



so = Solution()
print(so.countSteppingNumbers(low = "90", high = "101"))
print(so.countSteppingNumbers(low = "2", high = "40"))
print(so.countSteppingNumbers(low = "1", high = "11"))




