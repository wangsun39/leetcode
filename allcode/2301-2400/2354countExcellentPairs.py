# 给你一个下标从 0 开始的正整数数组 nums 和一个正整数 k 。
#
# 如果满足下述条件，则数对 (num1, num2) 是 优质数对 ：
#
# num1 和 num2 都 在数组 nums 中存在。
# num1 OR num2 和 num1 AND num2 的二进制表示中值为 1 的位数之和大于等于 k ，其中 OR 是按位 或 操作，而 AND 是按位 与 操作。
# 返回 不同 优质数对的数目。
#
# 如果a != c 或者 b != d ，则认为 (a, b) 和 (c, d) 是不同的两个数对。例如，(1, 2) 和 (2, 1) 不同。
#
# 注意：如果 num1 在数组中至少出现 一次 ，则满足 num1 == num2 的数对 (num1, num2) 也可以是优质数对。
#
# 
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3
# 输出：5
# 解释：有如下几个优质数对：
# - (3, 3)：(3 AND 3) 和 (3 OR 3) 的二进制表示都等于 (11) 。值为 1 的位数和等于 2 + 2 = 4 ，大于等于 k = 3 。
# - (2, 3) 和 (3, 2)： (2 AND 3) 的二进制表示等于 (10) ，(2 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
# - (1, 3) 和 (3, 1)： (1 AND 3) 的二进制表示等于 (01) ，(1 OR 3) 的二进制表示等于 (11) 。值为 1 的位数和等于 1 + 2 = 3 。
# 所以优质数对的数目是 5 。
# 示例 2：
#
# 输入：nums = [5,1,1], k = 10
# 输出：0
# 解释：该数组中不存在优质数对。
# 
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 60

from leetcode.allcode.competition.mypackage import *

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def count(num):
            cnt = 0
            while num:
                num = num & (num - 1)
                cnt += 1
            return cnt
        ans = 0
        nums = set(nums)
        bits = [count(e) for e in nums]
        counter = Counter(bits)
        for k1 in counter:
            for k2 in counter:
                if k1 + k2 < k:
                    continue
                ans += (counter[k1] * counter[k2])

        return ans

    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        nums = list(set(nums))
        nums2 = [x.bit_count() for x in nums]
        nums2.sort()
        ans = 0
        for i, x in enumerate(nums2):
            y = k - x
            p = bisect_left(nums2, y)
            ans += (len(nums) - p)
        return ans


so = Solution()
print(so.countExcellentPairs([1,536870911], 30))
print(so.countExcellentPairs([1,2,4,8,16,32,64,128,256], 2))
print(so.countExcellentPairs(nums = [1,2,3,1], k = 3))
print(so.countExcellentPairs(nums = [5,1,1], k = 10))




