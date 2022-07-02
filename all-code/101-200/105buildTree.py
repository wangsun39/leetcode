from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(preorder, inorder):
            if 0 == len(preorder):
                return None
            root = TreeNode(preorder[0])
            idxIn = inorder.index(preorder[0])
            root.left = recur(preorder[1:1 + idxIn], inorder[:idxIn])
            root.right = recur(preorder[1 + idxIn:], inorder[idxIn + 1:])
            return root
        if 0 == len(preorder):
            return None

        return recur(preorder, inorder)



so = Solution()
print(so.buildTree([3,9,20,15,7], [9,3,15,20,7]))