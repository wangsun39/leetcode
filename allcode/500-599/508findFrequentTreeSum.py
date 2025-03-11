# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#
#
#
# 示例 1：
# 输入:
#
#   5
#  /  \
# 2   -3
# 返回[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
# 示例2：
# 输入：
#
#   5
#  /  \
# 2   -5
# 返回[2]，只有 2 出现两次，-5 只出现 1 次。
#
#
#
# 提示：假设任意子树元素和均可以用 32 位有符号整数表示。


from leetcode.allcode.competition.mypackage import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def findFrequentTreeSum1(self, root: TreeNode) -> List[int]:
        dictSum = defaultdict(int) # sum: count 某种子树和对应的次数
        def helper(node):
            if node is None:
                return 0
            curSum = node.val + helper(node.left) + helper(node.right)
            dictSum[curSum] += 1
            return curSum
        helper(root)
        maxSum = None
        res = []
        for k in dictSum:
            if maxSum is None or maxSum < dictSum[k]:
                maxSum = dictSum[k]
                res = [k]
            elif maxSum == dictSum[k]:
                res.append(k)

        return res

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:  # 2022.6.19
        sumArray = []

        def helper(node):
            if node is not None:
                s = node.val + helper(node.left) + helper(node.right)
                sumArray.append(s)
                return s
            return 0

        helper(root)
        counter = Counter(sumArray)
        res = counter.most_common(1)[0][1]

        return [s for s, c in counter.items() if c == res]

so = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(so.findFrequentTreeSum(root))

