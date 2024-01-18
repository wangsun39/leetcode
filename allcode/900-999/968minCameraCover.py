# 给定一个二叉树，我们在树的节点上安装摄像头。
#
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
#
# 计算监控树的所有节点所需的最小摄像头数量。
#
#
#
# 示例 1：
#
#
#
# 输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。
# 示例 2：
#
#
#
# 输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
#
# 提示：
#
# 给定树的节点数的范围是 [1, 1000]。
# 每个节点的值都是 0。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode, type):
            # type: 1 表示node需要安装
            #       2 表示node不需要安装，且node已被覆盖
            #       3 表示node不需要安装，且node未被覆盖
            if type == 1:
                if node.left is None and node.right is None:
                    return 1
                res = 1
                if node.left:
                    res += min(dfs(node.left, 1), dfs(node.left, 2))
                if node.right:
                    res += min(dfs(node.right, 1), dfs(node.right, 2))
            elif type == 2:
                if node.left is None and node.right is None:
                    return 0
                res = 0
                if node.left:
                    res += min(dfs(node.left, 1), dfs(node.left, 3))
                if node.right:
                    res += min(dfs(node.right, 1), dfs(node.right, 3))
            else:
                if node.left is None and node.right is None:
                    return inf
                if node.left is None:
                    return dfs(node.right, 1)
                if node.right is None:
                    return dfs(node.left, 1)
                res = min(dfs(node.left, 1) + dfs(node.right, 1), dfs(node.left, 1) + dfs(node.right, 3), dfs(node.left, 3) + dfs(node.right, 1))
            return res
        return min(dfs(root,1), dfs(root, 3))


so = Solution()
print(so.minCameraCover())




