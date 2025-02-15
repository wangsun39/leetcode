# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
#
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
#
#
#
# 示例 1：
#
# 输入：nums = [3,6,9,12]
# 输出：4
# 解释：
# 整个数组是公差为 3 的等差数列。
# 示例 2：
#
# 输入：nums = [9,4,7,2,10]
# 输出：3
# 解释：
# 最长的等差子序列是 [4,7,10]。
# 示例 3：
#
# 输入：nums = [20,1,15,3,10,5,8]
# 输出：4
# 解释：
# 最长的等差子序列是 [20,15,10,5]。
#
#
# 提示：
#
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500

from leetcode.allcode.competition.mypackage import *

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        i = 0  # 记录处理到字符串的位置

        def dfs(lev) -> [TreeNode, int]:  # 返回当前节点和下一个即将处理的点的层级
            nonlocal i
            v = 0
            while i < n and traversal[i] != '-':
                v = v * 10 + int(traversal[i])
                i += 1
            node = TreeNode(v)
            if i >= n - 1:
                return node, -1
            j = i
            while traversal[j] == '-':
                j += 1
            next_lev = j - i
            i = j
            if next_lev > lev:
                left, next_lev = dfs(next_lev)
                node.left = left
            if next_lev > lev:
                right, next_lev = dfs(next_lev)
                node.right = right
            return node, next_lev

        root, _ = dfs(0)
        return root


obj = Solution()
print(obj.recoverFromPreorder("1-2--3--4-5--6--7"))

