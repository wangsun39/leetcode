# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#     3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# 输出: 9
# 解释:小偷一晚能够盗取的最高金额= 4 + 5 = 9.
from functools import cache
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rob1(self, root: TreeNode) -> int:
        def helper(node):  # return 以当前节点为根节点的子树的rob值，以当前节点左子树为根节点的子树的rob值，以当前节点右子树为根节点的子树的rob值，
            if node is None:
                return 0, 0, 0
            if node.left is None and node.right is None:
                return node.val, 0, 0
            left, right, ll, lr, rl, rr = 0, 0, 0, 0, 0, 0
            if node.left is not None:
                left, ll, lr = helper(node.left)
            if node.right is not None:
                right, rl, rr = helper(node.right)
            # 当前的节点的rob值 = max(node.val + ll + lr + rl + rr, left + right)
            # 因为 如果node.left在最终集合中，则rob = left + right，同理node.right在最终集合中，也是一样
            # 否则，node.left/node.right都不在最终集合中，那么node肯定在最终集合中，那么rob = node.val + ll + lr + rl + rr
            return max(node.val + ll + lr + rl + rr, left + right), left, right
        return helper(root)[0]

    def rob(self, root: Optional[TreeNode]) -> int:
        # 2023/9/18 记忆化搜索
        @cache
        def dfs(node, flg):  # 从node向下选择，flg表示node这个点是否行窃
            if not node: return 0
            l = dfs(node.left, False)
            r = dfs(node.right, False)
            if not flg:
                l = max(l, dfs(node.left, True))
                r = max(r, dfs(node.right, True))
                return l + r
            return node.val + l + r
        return max(dfs(root, True), dfs(root, False))


so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.rob(root))




