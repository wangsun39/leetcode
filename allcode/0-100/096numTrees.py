from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0: 1, 1: 1}
        for i in range(2, n + 1):
            cur = 0
            for j in range(i):
                cur += (dp[j] * dp[i-j-1])
            dp[i] = cur
        return dp[n]

so = Solution()

print(so.numTrees(3))
print(so.numTrees(8))
