# 给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。
#
# 你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：
#
# 从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。
#
# 注意：
#
# 查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。
# 树的高度是从根到树中某个节点的 最长简单路径中的边数 。
#
#
# 示例 1：
#
#
#
# 输入：root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
# 输出：[2]
# 解释：上图展示了从树中移除以 4 为根节点的子树。
# 树的高度是 2（路径为 1 -> 3 -> 2）。
# 示例 2：
#
#
#
# 输入：root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
# 输出：[3,2,3,2]
# 解释：执行下述查询：
# - 移除以 3 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 4）。
# - 移除以 2 为根节点的子树。树的高度变为 2（路径为 5 -> 8 -> 1）。
# - 移除以 4 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 6）。
# - 移除以 8 为根节点的子树。树的高度变为 2（路径为 5 -> 9 -> 3）。
#
#
# 提示：
#
# 树中节点的数目是 n
# 2 <= n <= 105
# 1 <= Node.val <= n
# 树中的所有值 互不相同
# m == queries.length
# 1 <= m <= min(n, 104)
# 1 <= queries[i] <= n
# queries[i] != root.val
# https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/

from typing import List
from typing import Optional
from cmath import inf
from collections import deque
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = {}
        nodeL = {}
        level = [[0] * 2 for _ in range(int(1e5) + 1)]
        def dfs(node, lv):
            l, r = 0, 0
            nodeL[node.val] = lv
            if node.left:
                l = dfs(node.left, lv + 1)
            if node.right:
                r = dfs(node.right, lv + 1)
            res = max(l, r) + 1
            height[node.val] = res
            if res > level[lv][0]:
                level[lv] = [res, level[lv][0]]
            elif res > level[lv][1]:
                level[lv][1] = res
            return res

        dfs(root, 0)
        ans = []
        for q in queries:
            lv = nodeL[q]
            x = level[lv][0]
            if height[q] == level[lv][0]:
                x = level[lv][1]
            ans.append(x + lv - 1)
        return ans



root = TreeNode(5)
root.left = TreeNode(8)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
root.left.right = TreeNode(1)
root.right = TreeNode(9)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

so = Solution()
print(so.treeQueries(root, [3,2,4,8]))




