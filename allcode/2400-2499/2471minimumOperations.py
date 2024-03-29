# 返回每一层按 严格递增顺序 排序所需的最少操作数目。
#
# 节点的 层数 是该节点和根节点之间的路径的边数。
#
#
#
# 示例 1 ：
#
#
# 输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# 输出：3
# 解释：
# - 交换 4 和 3 。第 2 层变为 [3,4] 。
# - 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。
# - 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。
# 共计用了 3 步操作，所以返回 3 。
# 可以证明 3 是需要的最少操作数目。
# 示例 2 ：
#
#
# 输入：root = [1,3,2,7,6,5,4]
# 输出：3
# 解释：
# - 交换 3 和 2 。第 2 层变为 [2,3] 。
# - 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。
# - 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。
# 共计用了 3 步操作，所以返回 3 。
# 可以证明 3 是需要的最少操作数目。
# 示例 3 ：
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：0
# 解释：每一层已经按递增顺序排序，所以返回 0 。
#
#
# 提示：
#
# 树中节点的数目在范围 [1, 105] 。
# 1 <= Node.val <= 105
# 树中的所有值 互不相同 。
from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
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

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	返回i的最后一位1
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶


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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level = [root]
        q = []
        qq = []
        ans = 0
        def calc(lev):
            nonlocal ans
            n = len(lev)
            d = {e: i for i, e in enumerate(lev)}
            # ast = [[e, i] for i, e in enumerate(lev)]
            ast = [e for e in lev]
            ast.sort()
            for i in range(n):
                if ast[i] == lev[i]:
                    continue
                idx = d[ast[i]]
                d[lev[i]], d[lev[idx]] = d[lev[idx]], d[lev[i]]
                lev[i], lev[idx] = lev[idx], lev[i]
                ans += 1
            return

        while True:
            while len(level):
                node = level.pop(0)
                if node.left:
                    q.append(node.left)
                    qq.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    qq.append(node.right.val)
            if len(q) == 0:
                break
            calc(qq)
            level, q, qq = q, [], []
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)

so = Solution()
print(so.minimumOperations(root))




