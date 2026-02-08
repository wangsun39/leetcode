# 给你一个长度为 n 的整数数组 nums ，n 是 偶数 ，同时给你一个整数 k 。
#
# 你可以对数组进行一些操作。每次操作中，你可以将数组中 任一 元素替换为 0 到 k 之间的 任一 整数。
#
# 执行完所有操作以后，你需要确保最后得到的数组满足以下条件：
#
# 存在一个整数 X ，满足对于所有的 (0 <= i < n) 都有 abs(a[i] - a[n - i - 1]) = X 。
# 请你返回满足以上条件 最少 修改次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,1,2,4,3], k = 4
#
# 输出：2
#
# 解释：
# 我们可以执行以下操作：
#
# 将 nums[1] 变为 2 ，结果数组为 nums = [1,2,1,2,4,3] 。
# 将 nums[3] 变为 3 ，结果数组为 nums = [1,2,1,3,4,3] 。
# 整数 X 为 2 。
#
# 示例 2：
#
# 输入：nums = [0,1,2,3,3,6,5,4], k = 6
#
# 输出：2
#
# 解释：
# 我们可以执行以下操作：
#
# 将 nums[3] 变为 0 ，结果数组为 nums = [0,1,2,0,3,6,5,4] 。
# 将 nums[4] 变为 4 ，结果数组为 nums = [0,1,2,0,4,6,5,4] 。
# 整数 X 为 4 。
#
#
#
# 提示：
#
# 2 <= n == nums.length <= 105
# n 是偶数。
# 0 <= nums[i] <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pair = []
        c1, c2 = Counter(), Counter()
        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            x = max(a, b, k - a, k - b)  # 修改a b 之一可能达到的最大差值
            pair.append([x, abs(a - b)])
            c2[abs(a - b)] += 1

        pair.sort()
        cur = 0
        m = n // 2
        mx = max(x for x, _ in pair)
        ans = n
        for x in range(mx + 1):  # 枚举X可能的值
            while cur < m and pair[cur][0] < x:
                c1[pair[cur][1]] += 1
                c2[pair[cur][1]] -= 1
                cur += 1
            # 在cur之前的要变2个元素，在cur之后的变一个元素，c1和c2中的都不要变
            v = (cur - c1[x]) * 2 + (m - cur - c2[x])
            ans = min(ans, v)
        return ans


so = Solution()
print(so.minChanges(nums = [1,0,1,2,4,3], k = 4))




