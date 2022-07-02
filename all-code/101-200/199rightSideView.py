from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        queue1, queue2 = [root], []
        while len(queue1) > 0:
            res.append(queue1[0].val)
            for x in queue1:
                if x.right is not None:
                    queue2.append(x.right)
                if x.left is not None:
                    queue2.append(x.left)
            queue1, queue2 = queue2, []
        return res


so = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
print(so.rightSideView(root))
