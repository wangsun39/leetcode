# 给你一个整数数组 banned 和两个整数 n 和 maxSum 。你需要按照以下规则选择一些整数：
#
# 被选择整数的范围是 [1, n] 。
# 每个整数 至多 选择 一次 。
# 被选择整数不能在数组 banned 中。
# 被选择整数的和不超过 maxSum 。
# 请你返回按照上述规则 最多 可以选择的整数数目。
#
#
#
# 示例 1：
#
# 输入：banned = [1,6,5], n = 5, maxSum = 6
# 输出：2
# 解释：你可以选择整数 2 和 4 。
# 2 和 4 在范围 [1, 5] 内，且它们都不在 banned 中，它们的和是 6 ，没有超过 maxSum 。
# 示例 2：
#
# 输入：banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
# 输出：0
# 解释：按照上述规则无法选择任何整数。
# 示例 3：
#
# 输入：banned = [11], n = 7, maxSum = 50
# 输出：7
# 解释：你可以选择整数 1, 2, 3, 4, 5, 6 和 7 。
# 它们都在范围 [1, 7] 中，且都没出现在 banned 中，它们的和是 28 ，没有超过 maxSum 。
#
#
# 提示：
#
# 1 <= banned.length <= 104
# 1 <= banned[i], n <= 104
# 1 <= maxSum <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s1 = set(range(1, n + 1))
        s2 = set(banned)
        s3 = s1 - s2
        ans = 0
        s = 0
        for x in sorted(list(s3)):
            if s + x <= maxSum:
                ans += 1
                s += x
            else:
                break
        return ans


so = Solution()
print(so.maxCount(banned = [1,6,5], n = 5, maxSum = 6))




