# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回3, 它的长度是路径 [4,2,1,3] 或者[5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
#



from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if node is None:
                return 0
            left, right = helper(node.left), helper(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        helper(root)
        return res

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.diameterOfBinaryTree(root))

