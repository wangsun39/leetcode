# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node的新值等于原树中大于或等于node.val的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 注意：本题和 1038:https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
#
#
#
# 示例 1：
#
#
#
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 示例 2：
#
# 输入：root = [0,null,1]
# 输出：[1,null,1]
# 示例 3：
#
# 输入：root = [1,0,2]
# 输出：[3,3,2]
# 示例 4：
#
# 输入：root = [3,2,4,1]
# 输出：[7,9,4,10]
#
#
# 提示：
#
# 树中的节点数介于 0和 104之间。
# 每个节点的值介于 -104和104之间。
# 树中的所有值 互不相同 。
# 给定的树为二叉搜索树。


from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def convertBST1(self, root: TreeNode) -> TreeNode:
        curSum = 0
        if root is None:
            return root
        def helper(node):
            nonlocal curSum
            if node.right is not None:
                helper(node.right)
            node.val += curSum
            curSum = node.val
            if node.left is not None:
                helper(node.left)
        helper(root)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 2025/3/15 换个写法
        def dfs(node, base):  # 传入当前节点，及前面累计需要加的值，返回当前节点的子树总值（即当前节点左子树更新后的val或当前节点更新后的val）
            if node.right:
                node.val += dfs(node.right, base)
            else:
                node.val += base
            if node.left:
                return dfs(node.left, node.val)
            return node.val

        if root: dfs(root, 0)
        return root

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.convertBST(root))

