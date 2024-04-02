# 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。
#
# 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。
#
# 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。
#
#
#
# 示例 1：
#
#
# 输入：n = 7
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 示例 2：
#
# 输入：n = 3
# 输出：[[0,0,0]]
#
#
# 提示：
#
# 1 <= n <= 20

from leetcode.allcode.competition.mypackage import *

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def copyTree(node):
            if node is None: return None
            res = TreeNode(0)
            res.left = copyTree(node.left)
            res.right = copyTree(node.right)
            return res

        tree = defaultdict(list)
        tree[1] = [TreeNode(0)]
        for i in range(3, n + 1, 2):
            for left in range(1, i, 2):
                right = i - 1 - left
                for tl in tree[left]:
                    for tr in tree[right]:
                        r = TreeNode(0)
                        r.left = copyTree(tl)
                        r.right = copyTree(tr)
                        tree[i].append(r)
        return tree[n]




        # @cache
        # def dfs(x, num):
        #     if num == 1:
        #         return [TreeNode(0)]
        #     res = []
        #     for i in range(1, num - 1):
        #         left = TreeNode(0)
        #         r1 = dfs(left, i)
        #         right = TreeNode(0)
        #         r2 = dfs(right, num - i - 1)
        #         for u in r1:
        #             x.left = u
        #             for v in r2:
        #                 x.right = v
        #                 res.append(x)
        #         # x.left = x.right = None
        #     return res
        # return dfs(TreeNode(0), n)



so = Solution()
print(so.allPossibleFBT(7))




