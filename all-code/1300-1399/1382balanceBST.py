# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。
#
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
# 示例 2：
#
#
#
# 输入: root = [2,1,3]
# 输出: [2,1,3]
#
#
# 提示：
#
# 树节点的数目在 [1, 104] 范围内。
# 1 <= Node.val <= 105
from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if node is None: return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        l = dfs(root)
        n = len(l)
        def dfs2(i, j):
            mid = (i + j) // 2
            left = right = None
            if i < mid:
                left = dfs2(i, mid - 1)
            if mid < j:
                right = dfs2(mid + 1, j)
            m = TreeNode(l[mid])
            m.left = left
            m.right = right
            return m
        return dfs2(0, n - 1)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)




so = Solution()
t = so.balanceBST(root)
print(t)

