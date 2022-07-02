from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recur(inorder, postorder):
            if 0 == len(postorder):
                return None
            root = TreeNode(postorder[-1])
            idxIn = inorder.index(postorder[-1])
            root.left = recur(inorder[:idxIn], postorder[:idxIn])
            root.right = recur(inorder[idxIn + 1:], postorder[idxIn:-1])
            return root
        if 0 == len(inorder):
            return None

        return recur(inorder, postorder)



so = Solution()
print(so.buildTree([9,3,15,20,7], [9,15,7,20,3]))