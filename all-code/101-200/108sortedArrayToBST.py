from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums):
            if 0 == len(nums):
                return None
            N = len(nums)
            mid = N // 2
            node = TreeNode(nums[mid])
            node.left = helper(nums[:mid])
            node.right = helper(nums[mid+1:])
            return node
        res = helper(nums)
        return res


so = Solution()
print(so.sortedArrayToBST([-10,-3,0,5,9]))
