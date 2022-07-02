from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        curMax, curVal, curCnt, res = 0, None, 0, []
        def helper(node):
            nonlocal curMax, curVal, curCnt, res
            if node is None:
                return
            helper(node.left)
            if node.val == curVal:
                curCnt += 1
            else:
                curVal = node.val
                curCnt = 1

            if curCnt > curMax:
                curMax = curCnt
                res = [curVal]
            elif curCnt == curMax:
                res.append(curVal)
            helper(node.right)

        helper(root)
        return res

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.findMode(root))

