# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
#
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
#
# 叶子节点，就是没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
# 示例 2：
#
#
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]
# 示例 3：
#
#
# 输入：root = [1,2,-3,-5,null,4,null], limit = -1
# 输出：[1,null,-3,4]
#
#
# 提示：
#
# 树中节点数目在范围 [1, 5000] 内
# -105 <= Node.val <= 105
# -109 <= limit <= 109

from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node, val):
            if node.left is None and node.right is None:
                if val + node.val < limit:
                    return False
                return True
            l = r = False
            if node.left:
                l = dfs(node.left, val + node.val)
                if not l:
                    node.left = None
            if node.right:
                r = dfs(node.right, val + node.val)
                if not r:
                    node.right = None
            if not l and not r:
                return False
            return True
        ret = dfs(root, 0)
        return root if ret else []

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(-5)
root.right = TreeNode(-3)
root.right.left = TreeNode(4)

so = Solution()
print(so.sufficientSubset(root, -1))

