from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SubTreeNode(TreeNode):
    def __init__(self, x):
        TreeNode.__init__(self, x)
        self.parent = None
        self.sum = x

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if root is None:
            return res
        subRoot = SubTreeNode(root.val)
        def getPath(subRoot):
            path = []
            while subRoot is not None:
                path.insert(0, subRoot.val)
                subRoot = subRoot.parent
            return path
        def transTree(root, subRoot):
            nonlocal res
            if root.left is None and root.right is None:
                if subRoot.sum == sum:
                    res.append(getPath(subRoot))
                return
            if root.left is not None:
                subRoot.left = SubTreeNode(root.left.val)
                subRoot.left.parent = subRoot
                subRoot.left.sum += subRoot.sum
                transTree(root.left, subRoot.left)
            if root.right is not None:
                subRoot.right = SubTreeNode(root.right.val)
                subRoot.right.parent = subRoot
                subRoot.right.sum += subRoot.sum
                transTree(root.right, subRoot.right)
        transTree(root, subRoot)
        return res



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
so = Solution()
print(so.pathSum(root, 31))
print(so.pathSum(root, 30))

root = TreeNode(1)
root.left = TreeNode(2)
print(so.pathSum(root, 1))

