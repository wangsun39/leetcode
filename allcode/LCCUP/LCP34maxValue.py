# 小扣有一个根结点为 root 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 val 价值。小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 k 个，求所有染成蓝色的结点价值总和最大是多少？
#
# 示例 1：
#
# 输入：root = [5,2,3,4], k = 2
#
# 输出：12
#
# 解释：结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12image.png
#
# 示例 2：
#
# 输入：root = [4,1,3,9,null,null,2], k = 2
#
# 输出：16
#
# 解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16image.png
#
# 提示：
#
# 1 <= k <= 10
# 1 <= val <= 10000
# 1 <= 结点数量 <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def dfs(node):
            # 返回 与 node 连通的节点个数为 0 - k ，且都染色的情况下，子树的最大值（其中连通个数为0，表示node节点不染色）
            res = [0] * (k + 1)
            l, r = [0] * (k + 1), [0] * (k + 1)
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            res[0] = max(l) + max(r)
            for i in range(k):
                for j in range(k - i):
                    res[i + j + 1] = max(res[i + j + 1], l[i] + r[j] + node.val)
            return res

        ans = dfs(root)
        return max(ans)


so = Solution()
print(so.maxValue(bucket = [9,0,1], vat = [0,2,2]))




