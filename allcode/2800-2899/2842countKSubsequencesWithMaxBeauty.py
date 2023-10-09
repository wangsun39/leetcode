# 给你一个字符串 s 和一个整数 k 。
#
# k 子序列指的是 s 的一个长度为 k 的 子序列 ，且所有字符都是 唯一 的，也就是说每个字符在子序列里只出现过一次。
#
# 定义 f(c) 为字符 c 在 s 中出现的次数。
#
# k 子序列的 美丽值 定义为这个子序列中每一个字符 c 的 f(c) 之 和 。
#
# 比方说，s = "abbbdd" 和 k = 2 ，我们有：
#
# f('a') = 1, f('b') = 3, f('d') = 2
# s 的部分 k 子序列为：
# "abbbdd" -> "ab" ，美丽值为 f('a') + f('b') = 4
# "abbbdd" -> "ad" ，美丽值为 f('a') + f('d') = 3
# "abbbdd" -> "bd" ，美丽值为 f('b') + f('d') = 5
# 请你返回一个整数，表示所有 k 子序列 里面 美丽值 是 最大值 的子序列数目。由于答案可能很大，将结果对 109 + 7 取余后返回。
#
# 一个字符串的子序列指的是从原字符串里面删除一些字符（也可能一个字符也不删除），不改变剩下字符顺序连接得到的新字符串。
#
# 注意：
#
# f(c) 指的是字符 c 在字符串 s 的出现次数，不是在 k 子序列里的出现次数。
# 两个 k 子序列如果有任何一个字符在原字符串中的下标不同，则它们是两个不同的子序列。所以两个不同的 k 子序列可能产生相同的字符串。
#
#
# 示例 1：
#
# 输入：s = "bcca", k = 2
# 输出：4
# 解释：s 中我们有 f('a') = 1 ，f('b') = 1 和 f('c') = 2 。
# s 的 k 子序列为：
# bcca ，美丽值为 f('b') + f('c') = 3
# bcca ，美丽值为 f('b') + f('c') = 3
# bcca ，美丽值为 f('b') + f('a') = 2
# bcca ，美丽值为 f('c') + f('a') = 3
# bcca ，美丽值为 f('c') + f('a') = 3
# 总共有 4 个 k 子序列美丽值为最大值 3 。
# 所以答案为 4 。
# 示例 2：
#
# 输入：s = "abbcd", k = 4
# 输出：2
# 解释：s 中我们有 f('a') = 1 ，f('b') = 2 ，f('c') = 1 和 f('d') = 1 。
# s 的 k 子序列为：
# abbcd ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5
# abbcd ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5
# 总共有 2 个 k 子序列美丽值为最大值 5 。
# 所以答案为 2 。
#
#
# 提示：
#
# 1 <= s.length <= 2 * 105
# 1 <= k <= s.length
# s 只包含小写英文字母。

import math
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
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = Counter(s)
        n = len(cnt)
        if n < k: return 0
        l = [[x, c] for x, c in cnt.items()]
        l.sort(key=lambda x: [x[1]], reverse=True)
        mn = l[k - 1][1]  # 与第k项相同的字母都要包含进来
        i = 0
        while i < n and l[i][1] != mn:
            i += 1
        j = i  # 与第k项相同的开始下标
        i += 1
        while i < n and l[i][1] == mn:
            i += 1  # 与第k项相同的结束下标的后一个

        ans = 1
        for x, c in l[:j]:
            ans *= c
            ans %= MOD
        ans *= math.comb(i - j, k - j)  # 从[i, j)中选出k - j 个字母， 每种组合有 l[j][1] ^ k - j个子序列
        ans %= MOD
        ans *= (l[j][1] ** (k - j))

        return ans % MOD

so = Solution()
print(so.countKSubsequencesWithMaxBeauty("dpdemprzvz", 1))  # 1
print(so.countKSubsequencesWithMaxBeauty(s = "fkp", k = 2))  # 3
print(so.countKSubsequencesWithMaxBeauty(s = "abbcd", k = 4))  # 2
print(so.countKSubsequencesWithMaxBeauty(s = "bcca", k = 2))




