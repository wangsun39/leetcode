# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。
#
# 每分钟，如果节点满足以下全部条件，就会被感染：
#
# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
# 输出：4
# 解释：节点按以下过程被感染：
# - 第 0 分钟：节点 3
# - 第 1 分钟：节点 1、10、6
# - 第 2 分钟：节点5
# - 第 3 分钟：节点 4
# - 第 4 分钟：节点 9 和 2
# 感染整棵树需要 4 分钟，所以返回 4 。
# 示例 2：
#
#
# 输入：root = [1], start = 1
# 输出：0
# 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
#
#
# 提示：
#
# 树中节点的数目在范围 [1, 105] 内
# 1 <= Node.val <= 105
# 每个节点的值 互不相同
# 树中必定存在值为 start 的节点


from typing import List
from typing import Optional
from collections import deque
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
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree = defaultdict(set)
        def construct(node: TreeNode):
            array = [node]
            while len(array) > 0:
                cur = array.pop(0)
                if cur.left is not None:
                    tree[cur.val].add(cur.left.val)
                    tree[cur.left.val].add(cur.val)
                    array.append(cur.left)
                if cur.right is not None:
                    tree[cur.val].add(cur.right.val)
                    tree[cur.right.val].add(cur.val)
                    array.append(cur.right)

        def bfs(val):
            ans = 0
            infect = set()
            array = [val, '#']
            while len(array) > 1:
                cur = array.pop(0)
                if cur == '#':
                    ans += 1
                    array.append('#')
                    continue
                infect.add(cur)
                for e in tree[cur]:
                    if e not in infect:
                        array.append(e)
            return ans

        construct(root)
        return bfs(start)

root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)


so = Solution()
print(so.amountOfTime(root, 3))




