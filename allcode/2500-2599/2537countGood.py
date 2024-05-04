# 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中 好 子数组的数目。
#
# 一个子数组 arr 如果有 至少 k 对下标 (i, j) 满足 i < j 且 arr[i] == arr[j] ，那么称它是一个 好 子数组。
#
# 子数组 是原数组中一段连续 非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], k = 10
# 输出：1
# 解释：唯一的好子数组是这个数组本身。
# 示例 2：
#
# 输入：nums = [3,1,4,3,2,2,4], k = 2
# 输出：4
# 解释：总共有 4 个不同的好子数组：
# - [3,1,4,3,2,2] 有 2 对。
# - [3,1,4,3,2,2,4] 有 3 对。
# - [1,4,3,2,2,4] 有 2 对。
# - [4,3,2,2,4] 有 2 对。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countGood1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = 0
        counter = defaultdict(int)
        ans = 0
        pair_num = 0
        for cur in range(n):
            counter[nums[cur]] += 1
            pair_num += (counter[nums[cur]] - 1)
            if pair_num < k:
                ans += start  # 这步很关键
                continue
            while start < cur and pair_num >= k:  # 始终保证 [start, cur] 不是一个好子数组，但[start - 1, cur] 是好子数组
                pair_num -= (counter[nums[start]] - 1)
                counter[nums[start]] -= 1
                start += 1
            ans += start

        return ans

    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        counter = Counter()
        acc = 0  # [left, right] 区间内相等下标对的数目
        ans = 0
        for right, x in enumerate(nums):
            acc += (counter[x])
            counter[x] += 1
            while acc >= k:
                acc -= (counter[nums[left]] - 1)
                counter[nums[left]] -= 1
                left += 1
            ans += left
        return ans


so = Solution()
print(so.countGood(nums = [1,1,1,1,1], k = 10))  # 1
print(so.countGood([2,3,1,3,2], 1))   # 4
print(so.countGood([2,3,1,3,2,3,3,3,1,1,3,2,2,2], 18))   # 9
print(so.countGood(nums = [3,1,4,3,2,2,4], k = 2))  # 4




