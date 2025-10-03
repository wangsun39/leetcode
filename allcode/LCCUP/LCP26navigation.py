# 小扣参加的秋日市集景区共有 N 个景点，景点编号为 1~N。景点内设有 N−1 条双向道路，使所有景点形成了一个二叉树结构，根结点记为 root，景点编号即为节点值。
#
# 由于秋日市集景区的结构特殊，游客很容易迷路，主办方决定在景区的若干个景点设置导航装置，按照所在景点编号升序排列后定义装置编号为 1 ~ M。导航装置向游客发送数据，数据内容为列表 [游客与装置 1 的相对距离,游客与装置 2 的相对距离,...,游客与装置 M 的相对距离]。由于游客根据导航装置发送的信息来确认位置，因此主办方需保证游客在每个景点接收的数据信息皆不相同。请返回主办方最少需要设置多少个导航装置。
#
# 示例 1：
#
# 输入：root = [1,2,null,3,4]
#
# 输出：2
#
# 解释：在景点 1、3 或景点 1、4 或景点 3、4 设置导航装置。
#
# image.png
#
# 示例 2：
#
# 输入：root = [1,2,3,4]
#
# 输出：1
#
# 解释：在景点 3、4 设置导航装置皆可。
#
# image.png
#
# 提示：
#
# 2 <= N <= 50000
# 二叉树的非空节点值为 1~N 的一个排列。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def navigation(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if node is None: return 0
            if node.left is None and node.right is None: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left and node.right:
                if l == 0 and r == 0:
                    ans += 1
                    return 1
                if l == 0 or r == 0:
                    return 1
                return 2
            if node.left is None:
                return r
            if node.right is None:
                return l

        left, right = dfs(root.left), dfs(root.right)
        # if root.left and root.right:
        if left + right < 2:
            ans += 1

        return ans


so = Solution()


