# 给你一个二叉树的根节点root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
#
# 请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中最小 的那个。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,7,0,7,-8,null,null]
# 输出：2
# 解释：
# 第 1 层各元素之和为 1，
# 第 2 层各元素之和为 7 + 0 = 7，
# 第 3 层各元素之和为 7 + -8 = -1，
# 所以我们返回第 2 层的层号，它的层内元素之和最大。
# 示例 2：
#
# 输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
# 输出：2
#
#
# 提示：
#
# 树中的节点数在[1, 104]范围内
# -105<= Node.val <= 105




from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l1, l2 = deque([root]), deque()
        ans = [-1, 100000]
        level = 1
        while len(l1):
            levelSum = 0
            while len(l1):
                node = l1.popleft()
                levelSum += node.val
                if node.left:
                    l2.append(node.left)
                if node.right:
                    l2.append(node.right)
            if ans[0] < levelSum:
                ans = [levelSum, level]
            l1, l2 = l2, deque()
            level += 1
        return ans[1]



obj = Solution()
print(obj.maxLevelSum([1,-2], 3))


