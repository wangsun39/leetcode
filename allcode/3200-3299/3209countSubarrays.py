# 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中有多少个
# 子数组
# 满足：子数组中所有元素按位 AND 的结果为 k 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 1
#
# 输出：6
#
# 解释：
#
# 所有子数组都只含有元素 1 。
#
# 示例 2：
#
# 输入：nums = [1,1,2], k = 1
#
# 输出：3
#
# 解释：
#
# 按位 AND 值为 1 的子数组包括：[1,1,2], [1,1,2], [1,1,2] 。
#
# 示例 3：
#
# 输入：nums = [1,2,3], k = 2
#
# 输出：2
#
# 解释：
#
# 按位 AND 值为 2 的子数组包括：[1,2,3], [1,2,3] 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i], k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idx = [i for i, x in enumerate(nums) if x & k != k]  # 包含这些点的区间是不能满足要求的
        bits = []  # 保存k为0的bit位
        for i in range(32):
            if k & (1 << i) == 0:
                bits.append(i)
        idx.insert(0, -1)
        idx.append(n)
        def calc(arr):  # 计算一个子区间的所有子数组数
            if len(arr) == 0: return 0
            res = 0
            mx = {i: -1 for i in bits}  # mx[i] 记录bit位i为0的最右侧位置
            for i, x in enumerate(arr):
                # 枚举子区间的右端点，左端的最大值为所有 mx[i] 的最小值，这样才能保证所有bits上&之后都为0
                for j in bits:
                    if x & (1 << j) == 0:
                        mx[j] = i
                res += min(mx.values()) + 1
            return res

        ans = 0
        for a, b in pairwise(idx):
            ans += calc(nums[a + 1: b])  # 只需计算每个子区间的值

        return ans


so = Solution()
print(so.countSubarrays(nums = [9,1,8,9,5], k = 0))  # 7
print(so.countSubarrays(nums = [1,2,3], k = 2))  # 2
print(so.countSubarrays(nums = [1,9,9,7,4], k = 1))  # 6
print(so.countSubarrays(nums = [3,5,5,3,10], k = 0))  # 3
print(so.countSubarrays(nums = [2,1,2,4,0], k = 0))  # 11
print(so.countSubarrays(nums = [1,1,1], k = 1))  # 6
print(so.countSubarrays(nums = [1,1,2], k = 1))  # 3




