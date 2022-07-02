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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
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



so = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
#print(so.repeatedStringMatch("abcd", "cdabcdab"))
print(so.longestUnivaluePath(root))

