# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
#
# 如果指定节点没有对应的“下一个”节点，则返回null。
#
# 示例 1:
#
# 输入: root = [2,1,3], p = 1
#
#   2
#  / \
# 1   3
#
# 输出: 2
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], p = 6
#
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#
# 输出: null


from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        next = None
        cur = root
        def findLeft(node):
            if node is None:
                return None
            while node.left is not None:
                node = node.left
            return node
        while True:
            if cur.val == p.val:
                if p.right is None:
                    return next
                else:
                    return findLeft(p.right)
            elif cur.val > p.val:
                next = cur
                cur = cur.left
            else:
                cur = cur.right



root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

so = Solution()
print(so.inorderSuccessor(root, root.left).val)




