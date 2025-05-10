# 请实现一个函数来判断整数数组 postorder 是否为二叉搜索树的后序遍历结果。
#
#
#
# 示例 1：
#
#
#
# 输入: postorder = [4,9,6,5,8]
# 输出: false
# 解释：从上图可以看出这不是一颗二叉搜索树
# 示例 2：
#
#
#
# 输入: postorder = [4,6,5,9,8]
# 输出: true
# 解释：可构建的二叉搜索树如上图
#
#
# 提示：
#
# 数组长度 <= 1000
# postorder 中无重复数字

from leetcode.allcode.competition.mypackage import *

class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        n = len(postorder)
        def check(start, end):
            if start == end:
                return True
            idx1, idx2 = -1, -1  # 大于 postorder[end] 的最小下标， 小于 postorder[end] 的最大下标
            for i in range(start, end):
                if postorder[i] < postorder[end]: idx2 = i
                elif postorder[i] > postorder[end] and idx1 == -1: idx1 = i
            if idx1 == -1 or idx2 == -1:
                return check(start, end - 1)
            if idx1 < idx2: return False
            return check(start, idx2) and check(idx1, end - 1)
        if n <= 1: return True
        return check(0, n - 1)



so = Solution()
print(so. verifyTreeOrder([4,9,6,5,8]))




