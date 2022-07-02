# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        def helper(node, isLeft):
            nonlocal res
            if node is None:
                return
            if node.left is None and node.right is None:
                if isLeft:
                    res += node.val
                return
            helper(node.left, True)
            helper(node.right, False)
        helper(root, False)
        return res

