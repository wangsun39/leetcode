# 「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。
# 给定一棵二叉树 root 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。
#
# 示例 1：
#
# 输入：root = [1,3,2,1,null,2]
#
# 输出：3
#
# 解释：焰火中有 3 个不同的颜色，值分别为 1、2、3
#
# 示例 2：
#
# 输入：root = [3,3,3]
#
# 输出：1
#
# 解释：焰火中仅出现 1 个颜色，值为 3
#
# 提示：
#
# 1 <= 节点个数 <= 1000
# 1 <= Node.val <= 1000






from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
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

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root: TreeNode) -> int:
        ans = set()
        def dfs(node):
            if node is None:
                return
            ans.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(ans)


so = Solution()





