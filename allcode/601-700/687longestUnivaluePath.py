# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:
#
# 2
# 示例 2:
#
# 输入:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:
#
# 2
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath1(self, root: TreeNode) -> int:
        longest = 0
        def helper(node): # 返回值，一个是从node开始的最长路径，不包含经过node的路径
            nonlocal longest
            l, r = 0, 0
            if node.left is not None:
                d = helper(node.left)
                if node.val == node.left.val:
                    l = d + 1
            if node.right is not None:
                d = helper(node.right)
                if node.val == node.right.val:
                    r = d + 1
            longest = max(longest, l + r)
            return max(l, r)
        if root is not None:
            helper(root)
        return longest
    def longestUnivaluePath2(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            a1, a2 = 1, 1
            if node.left:
                l1, l2 = helper(node.left)
                if node.val == node.left.val:
                    a1 += l1
                a2 = max(a2, l2, a1)
            if node.right:
                r1, r2 = helper(node.right)
                if node.val == node.right.val:
                    a1 = max(a1, 1 + r1)
                a2 = max(a2, r2, a1)
            # a2 = max(l2, r2, a1)
            if node.left and node.right and node.val == node.left.val == node.right.val:
                a2 = max(a2, l1 + r1 + 1)
            return a1, a2  # a1 为以node为起点的最长路径上的点数，a2就是答案期望的路径上的点数
        if root is None:
            return 0
        x, y = helper(root)
        return y - 1

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 2023/4/19 树形 DP
        ans = 0
        def dfs(x):
            if x is None:return 0
            nonlocal ans
            l = r = res = 0
            if x.left:
                res = dfs(x.left)
                if x.val == x.left.val:
                    l = res
            if x.right:
                res = dfs(x.right)
                if x.val == x.right.val:
                    r = res
            ans = max(ans, l + r + 1)
            return max(l, r) + 1
        dfs(root)
        return ans - 1 if ans > 0 else 0


so = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
# root.right.right = TreeNode(5)
#print(so.repeatedStringMatch("abcd", "cdabcdab"))
print(so.longestUnivaluePath(root))

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
#print(so.repeatedStringMatch("abcd", "cdabcdab"))
print(so.longestUnivaluePath(root))

