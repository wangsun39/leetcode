# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
#
# 给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,1], k = 1
# 输出：0
# 解释：数对和对应的距离如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 距离第 1 小的数对是 (1,1) ，距离为 0 。
# 示例 2：
#
# 输入：nums = [1,1,1], k = 2
# 输出：0
# 示例 3：
#
# 输入：nums = [1,6,1], k = 3
# 输出：5
#
#
# 提示：
#
# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2



from leetcode.allcode.competition.mypackage import *
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def count(start, dist):  # 找到下标比start大，且与nums[start]距离 <= dist的数的个数
            target = nums[start] + dist
            pos = bisect.bisect_right(nums, target, start)
            return pos - start - 1
        def countD(dist):
            ans = 0
            for i in range(n):
                ans += count(i, dist)
                if ans > k:
                    return ans
            return ans
        low, high = 0, nums[n - 1] - nums[0] + 1
        while high > low:
            mid = (high + low) // 2
            if k > countD(mid):
                low = mid + 1
            # elif k < countD(mid):
            else:
                high = mid
        return low


so = Solution()
print(so.smallestDistancePair([1,1,1], k = 2))
print(so.smallestDistancePair([62,100,4], 2))
print(so.smallestDistancePair([1,6,1], k = 3))
print(so.smallestDistancePair([1,3,1], 1))

