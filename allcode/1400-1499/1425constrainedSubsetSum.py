# 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。
#
# 数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。
#
#
#
# 示例 1：
#
# 输入：nums = [10,2,-10,5,20], k = 2
# 输出：37
# 解释：子序列为 [10, 2, 5, 20] 。
# 示例 2：
#
# 输入：nums = [-1,-2,-3], k = 1
# 输出：-1
# 解释：子序列必须是非空的，所以我们选择最大的数字。
# 示例 3：
#
# 输入：nums = [10,-2,-10,-5,20], k = 2
# 输出：23
# 解释：子序列为 [10, -2, -5, 20] 。
#
#
# 提示：
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

from leetcode.allcode.competition.mypackage import *

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([[nums[0], 0]])  # 元素 [a, b] 表示以nums[b]结尾的最大子序列和为a, 对于a，单调减
        ans = nums[0]
        for i, x in enumerate(nums[1:], 1):
            while q and i - q[0][1] > k:
                q.popleft()
            if q:
                cur = max(q[0][0] + x, x)
            else:
                cur = x
            ans = max(ans, cur)
            while q and q[-1][0] <= cur:
                q.pop()
            q.append([cur, i])
        return ans



so = Solution()
print(so.constrainedSubsetSum(nums = [-5266,4019,7336,-3681,-5767], k = 2))
print(so.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2))
print(so.constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2))
print(so.constrainedSubsetSum(nums = [-1,-2,-3], k = 1))




