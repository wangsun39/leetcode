# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if 0 == len(nums):
            return None
        cur_max = [0, nums[0]]
        for i, value in enumerate(nums):
            if cur_max[1] < value:
                cur_max = [i, value]
        node = TreeNode(cur_max[1])
        if cur_max[0] > 0:
            node.left = self.constructMaximumBinaryTree(nums[:cur_max[0]])
        if cur_max[0] < len(nums)-1:
            node.right = self.constructMaximumBinaryTree(nums[cur_max[0]+1:])
        return node

def printTree(node):
    if node is not None:
        print(node.val)
        printTree(node.left)
        printTree(node.right)

so = Solution()
printTree(so.constructMaximumBinaryTree([3,2,1,6,0,5]))

