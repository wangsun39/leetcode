# 给你一个长度为 n 下标从 0 开始的整数数组 receiver 和一个整数 k 。
#
# 总共有 n 名玩家，玩家 编号 互不相同，且为 [0, n - 1] 中的整数。这些玩家玩一个传球游戏，receiver[i] 表示编号为 i 的玩家会传球给编号为 receiver[i] 的玩家。玩家可以传球给自己，也就是说 receiver[i] 可能等于 i 。
#
# 你需要从 n 名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 恰好 k 次。
#
# 如果选择编号为 x 的玩家作为开始玩家，定义函数 f(x) 表示从编号为 x 的玩家开始，k 次传球内所有接触过球玩家的编号之 和 ，如果有玩家多次触球，则 累加多次 。换句话说， f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver(k)[x] 。
#
# 你的任务时选择开始玩家 x ，目的是 最大化 f(x) 。
#
# 请你返回函数的 最大值 。
#
# 注意：receiver 可能含有重复元素。
#
#
#
# 示例 1：
#
# 传递次数	传球者编号	接球者编号	x + 所有接球者编号
#  	 	 	2
# 1	2	1	3
# 2	1	0	3
# 3	0	2	5
# 4	2	1	6
#
#
# 输入：receiver = [2,0,1], k = 4
# 输出：6
# 解释：上表展示了从编号为 x = 2 开始的游戏过程。
# 从表中可知，f(2) 等于 6 。
# 6 是能得到最大的函数值。
# 所以输出为 6 。
# 示例 2：
#
# 传递次数	传球者编号	接球者编号	x + 所有接球者编号
#  	 	 	4
# 1	4	3	7
# 2	3	2	9
# 3	2	1	10
#
#
# 输入：receiver = [1,1,1,2,3], k = 3
# 输出：10
# 解释：上表展示了从编号为 x = 4 开始的游戏过程。
# 从表中可知，f(4) 等于 10 。
# 10 是能得到最大的函数值。
# 所以输出为 10 。
#
#
# 提示：
#
# 1 <= receiver.length == n <= 105
# 0 <= receiver[i] <= n - 1
# 1 <= k <= 1010

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
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        M = 36
        n = len(receiver)
        nt1 = [[0] * M for _ in range(n)]  # nt[i][j]  记录第 i 个玩家 传球 2 ** j 次后的玩家
        nt2 = [[0] * M for _ in range(n)]  # nt[i][j]  记录第 i 个玩家 传球 2 ** j 次经过的玩家之和 （不包括起点）
        for i in range(n):
            nt1[i][0] = receiver[i]
            nt2[i][0] = receiver[i]
        for j in range(1, M):
            for i in range(n):
                v = nt1[i][j - 1]
                nt1[i][j] = nt1[v][j - 1]
                nt2[i][j] += (nt2[i][j - 1] + nt2[v][j - 1])
        def f(start):
            idx = 0
            cur = start
            kk = k
            ans = start
            while kk:
                if kk & 1:
                    ans += nt2[cur][idx]
                    cur = nt1[cur][idx]
                kk >>= 1
                idx += 1
            return ans
        return max(f(x) for x in range(n))



so = Solution()
print(so.getMaxFunctionValue(receiver = [0], k = 10000000000))
print(so.getMaxFunctionValue(receiver = [1,1,1,2,3], k = 4))
print(so.getMaxFunctionValue(receiver = [1,1,1,2,3], k = 3))
print(so.getMaxFunctionValue(receiver = [2,0,1], k = 4))




