#
# 给定一个二叉树，根节点为第1层，深度为 1。在其第d层追加一行值为v的节点。
#
# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为v的左子树和右子树。
#
# 将N 原先的左子树，连接为新节点v 的左子树；将N 原先的右子树，连接为新节点v 的右子树。
#
# 如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
#
# 示例 1:
#
# 输入:
# 二叉树如下所示:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
# v = 1
#
# d = 2
#
# 输出:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5
#
# 示例 2:
#
# 输入:
# 二叉树如下所示:
#       4
#      /
#     2
#    / \
#   3   1
#
# v = 1
#
# d = 3
#
# 输出:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1
# 注意:
#
# 输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。
# 输入的二叉树至少有一个节点。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if 1 == d:
            node = TreeNode(v)
            node.left = root
            return node
        def Helper(node, level):
            if node is None:
                return
            if level < d - 1:
                Helper(node.left, level + 1)
                Helper(node.right, level + 1)
                return
            newNodeL = TreeNode(v)
            newNodeR = TreeNode(v)
            newNodeL.left = node.left
            newNodeR.right = node.right
            node.left = newNodeL
            node.right = newNodeR
            return
        Helper(root, 1)
        return root



