# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
#
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
#
#
#
# 示例 1：
#
#
# 输入：root = [2,2,5,null,null,5,7]
# 输出：5
# 解释：最小的值是 2 ，第二小的值是 5 。
# 示例 2：
#
#
# 输入：root = [2,2,2]
# 输出：-1
# 解释：最小的值是 2, 但是不存在第二小的值。
#
#
# 提示：
#
# 树中节点数目在范围 [1, 25] 内
# 1 <= Node.val <= 231 - 1
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)
#

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = -1
        def helper(node):
            nonlocal res
            if node is None:
                return
            if node.val > root.val:
                res = min(res, node.val) if res > 0 else node.val
                return
            helper(node.left)
            helper(node.right)
        helper(root)
        return res



root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)


so = Solution()
# so.trimBST(root, 1, 2)

root = TreeNode(45)
root.left = TreeNode(30)
root.left.left = TreeNode(10)
root.left.right = TreeNode(36)
root.right = TreeNode(46)

so.trimBST(root, 32, 44)

