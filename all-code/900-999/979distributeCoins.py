# 给你一个有 n 个结点的二叉树的根结点 root ，其中树中每个结点 node 都对应有 node.val 枚硬币。整棵树上一共有 n 枚硬币。
#
# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。移动可以是从父结点到子结点，或者从子结点移动到父结点。
#
# 返回使每个结点上 只有 一枚硬币所需的 最少 移动次数。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,0,0]
# 输出：2
# 解释：一枚硬币从根结点移动到左子结点，一枚硬币从根结点移动到右子结点。
# 示例 2：
#
#
# 输入：root = [0,3,0]
# 输出：3
# 解释：将两枚硬币从根结点的左子结点移动到根结点（两次移动）。然后，将一枚硬币从根结点移动到右子结点。
#
#
# 提示：
#
# 树中节点的数目为 n
# 1 <= n <= 100
# 0 <= Node.val <= n
# 所有 Node.val 的值之和是 n
from math import log
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):  # 返回以 node 为根的子树 的节点上和硬币数之差，表示从经过这个节点，需拿走的硬币数
            nonlocal ans
            if node is None:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            ans += abs(l + r + node.val - 1)
            return l + r + node.val - 1
        dfs(root)
        return ans

    def distributeCoins1(self, root: Optional[TreeNode]) -> int:
        # 2023/8/5 另一种递归的思路
        ans = 0
        def dfs(node: TreeNode):  # 返回以 node 为根的子树的节点上和硬币数
            nonlocal ans
            if node is None: return 0, 0
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)
            ans += (abs(l1 - l2) + abs(r1 - r2))
            return l1 + r1 + 1, l2 + r2 + node.val

        dfs(root)
        return ans

root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)


so = Solution()
print(so.distributeCoins(root))

