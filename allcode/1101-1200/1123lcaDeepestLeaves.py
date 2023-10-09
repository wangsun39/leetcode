# 给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。
#
# 回想一下：
#
# 叶节点 是二叉树中没有子节点的节点
# 树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
# 如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4]
# 输出：[2,7,4]
# 解释：我们返回值为 2 的节点，在图中用黄色标记。
# 在图中用蓝色标记的是树的最深的节点。
# 注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。
# 示例 2：
#
# 输入：root = [1]
# 输出：[1]
# 解释：根节点是树中最深的节点，它是它本身的最近公共祖先。
# 示例 3：
#
# 输入：root = [0,1,3,null,2]
# 输出：[2]
# 解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。
#
#
# 提示：
#
# 树中的节点数将在 [1, 1000] 的范围内。
# 0 <= Node.val <= 1000
# 每个节点的值都是 独一无二 的。
#
#
# 注意：本题与力扣 865 重复：https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/

import bisect
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth = {}  # 每个节点的深度
        sub_dep = {}  # 每个节点子树的深度

        def dfs(node, dep):
            if node is None:
                return -1
            # depth[node.val] = dep
            sd = max(dfs(node.left, dep + 1), dfs(node.right, dep + 1)) + 1
            sub_dep[node.val] = sd
            return sd
        dfs(root, 0)

        cur = root
        while True:
            if cur.left is None and cur.right is None:
                return cur
            if cur.left is None:
                cur = cur.right
            elif cur.right is None:
                cur = cur.left
            else:
                if sub_dep[cur.left.val] == sub_dep[cur.right.val]:
                    return cur
                elif sub_dep[cur.left.val] > sub_dep[cur.right.val]:
                    cur = cur.left
                else:
                    cur = cur.right

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 2023/9/6  LCA的写法
        n = 1001
        order = n.bit_length() + 1
        p = [[-1] * order for _ in range(n)]  # 记录每个节点的2 ^ i的祖
        dep = [-1] * n
        mx_dep = 0
        node_map = {}
        def dfs(node, lv):
            nonlocal mx_dep
            dep[node.val] = lv
            node_map[node.val] = node
            mx_dep = max(mx_dep, lv)
            if node.left is not None:
                p[node.left.val][0] = node.val
                dfs(node.left, lv + 1)
            if node.right is not None:
                p[node.right.val][0] = node.val
                dfs(node.right, lv + 1)
        dfs(root, 0)

        for j in range(order):
            for i in range(n):
                if p[i][j - 1] == -1: continue
                p[i][j] = p[p[i][j - 1]][j - 1]

        bottom = []
        for i in range(n):
            if dep[i] == mx_dep:
                bottom.append(i)
        def lca(x, y):
            if dep[x] > dep[y]:
                x, y = y, x
            for i in range(dep[y] - dep[x]):
                y = p[y][0]
            # x, y 在同一层
            if x == y: return x
            for i in range(order - 1, -1, -1):
                if p[x][i] == p[y][i]:
                    continue
                x, y = p[x][i], p[y][i]
            return p[x][0]
        ans = bottom[0]
        for x in bottom[1:]:
            ans = lca(ans, x)
        return node_map[ans]








root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.right = TreeNode(1)

so = Solution()
print(so.lcaDeepestLeaves(root))

root = TreeNode(1)

so = Solution()
print(so.lcaDeepestLeaves(root))

