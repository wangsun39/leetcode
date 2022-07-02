# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        def tree2arry(node):
            if node is None:
                return []
            return tree2arry(node.left) + [node.val] + tree2arry(node.right)
        array = tree2arry(root)
        print(array)
        N = len(array)
        left, right = 0, N-1
        while left < right:
            cur = array[left] + array[right]
            if cur == k:
                return True
            elif cur < k:
                left += 1
            else:
                right -= 1
        return False

def printTree(node):
    if node is not None:
        print(node.val)
        printTree(node.left)
        printTree(node.right)

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(so.findTarget(root, 9))
print(so.findTarget(root, 28))

