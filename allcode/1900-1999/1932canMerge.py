# 给你 n 个 二叉搜索树的根节点 ，存储在数组 trees 中（下标从 0 开始），对应 n 棵不同的二叉搜索树。trees 中的每棵二叉搜索树 最多有 3 个节点 ，且不存在值相同的两个根节点。在一步操作中，将会完成下述步骤：
#
# 选择两个 不同的 下标 i 和 j ，要求满足在 trees[i] 中的某个 叶节点 的值等于 trees[j] 的 根节点的值 。
# 用 trees[j] 替换 trees[i] 中的那个叶节点。
# 从 trees 中移除 trees[j] 。
# 如果在执行 n - 1 次操作后，能形成一棵有效的二叉搜索树，则返回结果二叉树的 根节点 ；如果无法构造一棵有效的二叉搜索树，返回 null 。
#
# 二叉搜索树是一种二叉树，且树中每个节点均满足下述属性：
#
# 任意节点的左子树中的值都 严格小于 此节点的值。
# 任意节点的右子树中的值都 严格大于 此节点的值。
# 叶节点是不含子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：trees = [[2,1],[3,2,5],[5,4]]
# 输出：[3,2,5,1,null,4]
# 解释：
# 第一步操作中，选出 i=1 和 j=0 ，并将 trees[0] 合并到 trees[1] 中。
# 删除 trees[0] ，trees = [[3,2,5,1],[5,4]] 。
#
# 在第二步操作中，选出 i=0 和 j=1 ，将 trees[1] 合并到 trees[0] 中。
# 删除 trees[1] ，trees = [[3,2,5,1,null,4]] 。
#
# 结果树如上图所示，为一棵有效的二叉搜索树，所以返回该树的根节点。
# 示例 2：
#
#
# 输入：trees = [[5,3,8],[3,2,6]]
# 输出：[]
# 解释：
# 选出 i=0 和 j=1 ，然后将 trees[1] 合并到 trees[0] 中。
# 删除 trees[1] ，trees = [[5,3,8,2,6]] 。
#
# 结果树如上图所示。仅能执行一次有效的操作，但结果树不是一棵有效的二叉搜索树，所以返回 null 。
# 示例 3：
#
#
# 输入：trees = [[5,4],[3]]
# 输出：[]
# 解释：无法执行任何操作。
#
#
# 提示：
#
# n == trees.length
# 1 <= n <= 5 * 104
# 每棵树中节点数目在范围 [1, 3] 内。
# 输入数据的每个节点可能有子节点但不存在子节点的子节点
# trees 中不存在两棵树根节点值相同的情况。
# 输入中的所有树都是 有效的二叉树搜索树 。
# 1 <= TreeNode.val <= 5 * 104.

from leetcode.allcode.competition.mypackage import *

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        root = {}
        leaf = {}
        values = set()
        for i, tree in enumerate(trees):
            root[tree.val] = i
            values.add(tree.val)
            if tree.left:
                if tree.left.val in leaf:
                    return None
                leaf[tree.left.val] = i
                values.add(tree.left.val)
            if tree.right:
                if tree.right.val in leaf:
                    return None
                leaf[tree.right.val] = i
                values.add(tree.right.val)

        n = len(trees)
        # 判断连通性
        fa = list(range(n))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for v in values:
            if v in root and v in leaf:
                union(root[v], leaf[v])
        for i in range(n):
            find(i)
        if any(x != fa[0] for x in fa):  # 判断整体是否连通
            return None

        def merge(i, j):  # i的根 和j的叶子合并
            if trees[j].left and trees[j].left.val == trees[i].val:
                trees[j].left = trees[i]
            else:
                trees[j].right = trees[i]

        ans = None
        for v in values:
            if v in root and v not in leaf:
                if ans: return None
                ans = trees[root[v]]
            if v in root and v in leaf:
                merge(root[v], leaf[v])

        if ans is None: return None

        def check(node):  # 检查node是否是BST
            l1 = r2 = node.val
            if node.left:
                ret, l1, l2 = check(node.left)
                if not ret or l2 > node.val:
                    return False, 0, 0
            if node.right:
                ret, r1, r2 = check(node.right)
                if not ret or r1 < node.val:
                    return False, 0, 0
            return True, l1, r2

        ret, _, _ = check(ans)
        if not ret: return None

        return ans

# trees = []
# t = TreeNode(2)
# t.left = TreeNode(1)
# trees.append(t)
# t = TreeNode(3)
# t.left = TreeNode(2)
# t.right = TreeNode(5)
# trees.append(t)
# t = TreeNode(5)
# t.left = TreeNode(4)
# trees.append(t)

trees = []
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(8)
trees.append(t)
t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(6)
trees.append(t)


so = Solution()
print(so.canMerge(trees))




