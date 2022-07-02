# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
#
# 示例 1:
# 给定的树 s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：
#
#    4
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
#
# 示例 2:
# 给定的树 s：
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给定的树 t：
#
#    4
#   / \
#  1   2
# 返回 false。



from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None or t1.val != t2.val:
                return False
            return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
        def helper(t1):
            if t1 is None:
                return False
            if isSame(t1, t):
                return True
            return helper(t1.left) or helper(t1.right)
        return helper(s)

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.isSubtree(root, root))

