
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为NULL 的节点将直接作为新二叉树的节点。
#
# 示例1:
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# 注意:合并必须从两个树的根节点开始。



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def Helper(t1, t2):
            if t1 is None:
                return t2
            elif t2 is None:
                return t1
            t3 = TreeNode(t1.val + t2.val)
            t3.left = Helper(t1.left, t2.left)
            t3.right = Helper(t1.right, t2.right)
            return t3
        return Helper(t1, t2)


