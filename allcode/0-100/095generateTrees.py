from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # dp[i] 表示子树节点个数是i的所有子树，dp[i][j] 表示子树节点个数是i的,且最小节点的val是j+1的所有子树
        dp = {0: [[None], [None], [None], [None], [None], [None], [None], [None], [None]]}
        for i in range(1, n + 1):  # i表示树的总节点个数
            dp[i] = []
            for k in range(n-i+1):  # 构造所有最小节点的val是k+1的子树
                cur = []
                for j in range(i):  # j表示根节点的左子树节点个数
                    for left in dp[j][k]:
                        for right in dp[i-j-1][j+k+1]:
                            x = TreeNode(j+k+1)
                            x.left = left
                            x.right = right
                            cur.append(x)
                dp[i].append(cur)
        return dp[n][0] if n > 0 else []

so = Solution()

print(so.generateTrees(8))
print(so.generateTrees(3))
