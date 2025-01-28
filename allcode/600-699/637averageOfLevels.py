# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
#
# 
#
# 示例 1：
#
# 输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue1, queue2 = [root], []
        rowSum = 0
        res = []
        while len(queue1) > 0:
            rowNum = len(queue1)
            while len(queue1) > 0:
                e = queue1.pop(0)
                rowSum += e.val
                if e.left is not None:
                    queue2.append(e.left)
                if e.right is not None:
                    queue2.append(e.right)
            queue1, queue2 = queue2, []
            res.append(rowSum / rowNum)
            rowSum = 0
        return res







