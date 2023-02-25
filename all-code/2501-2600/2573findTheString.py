# 对任一由 n 个小写英文字母组成的字符串 word ，我们可以定义一个 n x n 的矩阵，并满足：
#
# lcp[i][j] 等于子字符串 word[i,...,n-1] 和 word[j,...,n-1] 之间的最长公共前缀的长度。
# 给你一个 n x n 的矩阵 lcp 。返回与 lcp 对应的、按字典序最小的字符串 word 。如果不存在这样的字符串，则返回空字符串。
#
# 对于长度相同的两个字符串 a 和 b ，如果在 a 和 b 不同的第一个位置，字符串 a 的字母在字母表中出现的顺序先于 b 中的对应字母，则认为字符串 a 按字典序比字符串 b 小。例如，"aabd" 在字典上小于 "aaca" ，因为二者不同的第一位置是第三个字母，而 'b' 先于 'c' 出现。
#
#
#
# 示例 1：
#
# 输入：lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
# 输出："abab"
# 解释：lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。
# 示例 2：
#
# 输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
# 输出："aaaa"
# 解释：lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。
# 示例 3：
#
# 输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
# 输出：""
# 解释：lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。
#
#
# 提示：
#
# 1 <= n == lcp.length == lcp[i].length <= 1000
# 0 <= lcp[i][j] <= n

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
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        tmp = [''] * n
        ans = [''] * n
        ans[0] = tmp[0] = 'a'
        for i in range(n):
            if lcp[i][i] != n - i: return ''
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ''
                if lcp[i][j] > 0:
                    if lcp[i][j] > n - j:
                        return ''
                if i > 0 and j > 0 and lcp[i - 1][j - 1] > 0 and lcp[i][j] != lcp[i - 1][j - 1] - 1:
                    return ''
        for i in range(n):
            if ans[i] == '':
                ans[i] = tmp[i]
            for j in range(i + 1, n):
                if lcp[i][j] != 0:
                    if ans[j] != '' and ans[j] != ans[i]:
                        return ''
                    if ans[j] == '' and tmp[j] != '' and ord(tmp[j]) > ord(ans[i]):
                        return ''
                    ans[j] = ans[i]
                else:
                    if ans[j] != '' and ans[j] == ans[i]:
                        return ''
                    if tmp[j] == '':
                        tmp[j] = 'b'
                    else:
                        if ord(ans[i]) == ord(tmp[j]):
                            if ord(tmp[j]) == ord('z'):
                                return ''
                            tmp[j] = chr(ord(tmp[j]) + 1)
                    # tmp[j] = chr(ord(ans[i]) + 1)
        return ''.join(ans)


so = Solution()
print(so.findTheString([[15,0,1,0,1,1,1,1,1,0,0,1,0,1,1],[0,14,0,0,0,0,0,0,0,0,5,0,0,0,0],[1,0,13,0,1,1,1,1,2,0,0,4,0,1,1],[0,0,0,12,0,0,0,0,0,1,0,0,3,0,0],[1,0,1,0,11,4,3,2,1,0,0,1,0,2,1],[1,0,1,0,4,10,3,2,1,0,0,1,0,2,1],[1,0,1,0,3,3,9,2,1,0,0,1,0,2,1],[1,0,1,0,2,2,2,8,1,0,0,1,0,2,1],[1,0,2,0,1,1,1,1,7,0,0,2,0,1,1],[0,0,0,1,0,0,0,0,0,6,0,0,1,0,0],[0,5,0,0,0,0,0,0,0,0,5,0,0,0,0],[1,0,4,0,1,1,1,1,2,0,0,4,0,1,1],[0,0,0,3,0,0,0,0,0,1,0,0,3,0,0],[1,0,1,0,2,2,2,2,1,0,0,1,0,2,1],[1,0,1,0,1,1,1,1,1,0,0,1,0,1,1]]))  # ''
print(so.findTheString([[3, 2, 0], [2, 2, 0], [0, 0, 1]]))  # ''
print(so.findTheString([[3, 2, 0], [2, 2, 1], [0, 1, 1]]))  # ''
print(so.findTheString([[8,0,0,0,0,1,2,0],[0,7,0,1,1,0,0,1],[0,0,6,0,0,0,0,0],[0,1,0,5,1,0,0,1],[0,1,0,1,4,0,0,1],[1,0,0,0,0,3,1,0],[2,0,0,0,0,1,2,0],[0,1,0,1,1,0,0,1]]))  # "abcbbaab"
print(so.findTheString([[3, 0, 1], [0, 2, 1], [1, 1, 1]]))  # ''
print(so.findTheString([[2,2],[2,1]]))  # ''
print(so.findTheString([[4,1,1,1],[1,3,1,1],[1,1,2,1],[1,1,1,1]]))  # ''
print(so.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))
print(so.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]))  # abab
print(so.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]))  # aaaa




