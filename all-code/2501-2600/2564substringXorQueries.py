# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。
#
# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^ firsti == secondi 。
#
# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 lefti 最小的一个。
#
# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。
#
# 子字符串 是一个字符串中一段连续非空的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "101101", queries = [[0,5],[1,2]]
# 输出：[[0,2],[2,3]]
# 解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5 ，所以第一个查询的答案为 [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3 ，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3] 。
# 示例 2：
#
# 输入：s = "0101", queries = [[12,8]]
# 输出：[[-1,-1]]
# 解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。
# 示例 3：
#
# 输入：s = "1", queries = [[4,5]]
# 输出：[[0,0]]
# 解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0] 。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= queries.length <= 105
# 0 <= firsti, secondi <= 109

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

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, idx, word: str) -> None:  # O(log(len(word)))
        cur = self.root
        for e in word:
            if e not in cur:
                cur[e] = {}
            cur = cur[e]
        if 'end' in cur:
            cur['end'].append(idx)
        else:
            cur['end'] = [idx]


    def search(self, word: str) -> list:
        cur = self.root
        ans = []
        for e in word:
            if e in cur:
                cur = cur[e]
                if 'end' in cur:
                    ans += cur['end']
            else:
                return ans
        return ans


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        target = []
        for x, y in queries:
            target.append(bin(x ^ y)[2:])
        # print(target)
        tr = Trie()
        for i, t in enumerate(target):
            tr.insert(i, t)

        n = len(s)
        ans = [[-1, -1] for _ in range(len(queries))]
        for i in range(n):
            ids = tr.search(s[i:])
            if len(ids) == 0:
                continue
            for x in ids:
                if ans[x] != [-1, -1]:
                    continue
                ans[x] = [i, i + len(target[x]) - 1]
        return ans


        # ans = []
        # for t in target:
        #     pos = find(s, t)
        #     if pos == -1:
        #         ans.append([-1, -1])
        #     else:
        #         ans.append([pos, pos + len(t) - 1])
        # return ans



so = Solution()
print(so.substringXorQueries(s = "101101", queries = [[0,5],[1,2]]))
print(so.substringXorQueries(s = "0101", queries = [[12,8]]))
print(so.substringXorQueries(s = "1", queries = [[4,5]]))



