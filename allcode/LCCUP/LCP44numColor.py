# 「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。
# 给定一棵二叉树 root 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。
#
# 示例 1：
#
# 输入：root = [1,3,2,1,null,2]
#
# 输出：3
#
# 解释：焰火中有 3 个不同的颜色，值分别为 1、2、3
#
# 示例 2：
#
# 输入：root = [3,3,3]
#
# 输出：1
#
# 解释：焰火中仅出现 1 个颜色，值为 3
#
# 提示：
#
# 1 <= 节点个数 <= 1000
# 1 <= Node.val <= 1000






from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numColor(self, root: TreeNode) -> int:
        ans = set()
        def dfs(node):
            if node is None:
                return
            ans.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(ans)


so = Solution()





