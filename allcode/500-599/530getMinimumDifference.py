# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#
#
#
# 示例：
#
# 输入：
#
#    1
#     \
#      3
#     /
#    2
#
# 输出：
# 1
#
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
# 提示：
#
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre, cur, res = None, None, None
        def helper(node):
            nonlocal pre, cur, res
            if node.left is not None:
                helper(node.left)
            if pre is None:
                pre = node.val
            elif cur is None:
                cur = node.val
                res = abs(cur - pre)
            else:
                pre, cur = cur, node.val
                res = min(res, abs(cur - pre))
            if node.right is not None:
                helper(node.right)
        helper(root)
        return res

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.getMinimumDifference(root))

