# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
#
# 如果存在多个答案，您可以返回其中 任何 一个。
#
#
#
# 示例 1：
#
#
#
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 示例 2:
#
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#
#
# 提示：
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历

from leetcode.allcode.competition.mypackage import *

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d1 = {x: i for i, x in enumerate(preorder)}
        d2 = {x: i for i, x in enumerate(postorder)}
        n = len(postorder)

        def dfs(pre1, pre2, post1, post2):
            if pre1 > pre2:
                return None
            root = TreeNode(preorder[pre1])
            if pre1 == pre2:
                return root
            if preorder[pre1 + 1] == postorder[post2 - 1]:
                root.left = dfs(pre1 + 1, pre2, post1, post2 - 1)
            else:
                p1 = d1[postorder[post2 - 1]]
                p2 = d2[preorder[pre1 + 1]]
                root.left = dfs(pre1 + 1, p1 - 1, post1, p2)
                root.right = dfs(p1, pre2, p2 + 1, post2 - 1)
            return root
        return dfs(0, n - 1, 0, n - 1)



so = Solution()
print(so.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]))




