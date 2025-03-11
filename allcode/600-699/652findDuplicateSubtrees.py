# Definition for a binary tree node.
from leetcode.allcode.competition.mypackage import *
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        treeMap = defaultdict()
        treeMap.default_factory = treeMap.__len__
        count = defaultdict(int)
        res = []
        def buildMap(node):
            if node is None:
                return None
            uid = treeMap[(node.val, buildMap(node.left), buildMap(node.right))]
            count[uid] += 1
            if 2 == count[uid]:
                res.append(node)
            return uid
        buildMap(root)
        return res




def printTree(node):
    for i in node:
        print(i.val)

so = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
printTree(so.findDuplicateSubtrees(root))


