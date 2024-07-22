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
        div = []
        n = len(nums)
        for i, x in enumerate(nums):
            if x & k != k:  # 任何子数组都不会包含这种 x
                div.append(i)
        if not div or div[0] > 0:
            div.insert(0, -1)
        div.append(n)
        ans = 0
        def calc(start, end):   # 计算 [start, end) 区间内的子数组个数
            if start >= end:
                return 0
            counter = Counter()
            def add(num):
                i = 0
                while num:
                    if num & 1:
                        counter[i] += 1
                    i += 1
                    num >>= 1
            def remove(num):
                i = 0
                while num:
                    if num & 1:
                        counter[i] -= 1
                    i += 1
                    num >>= 1
            def trans():  # counter 转成数字
                res = 0
                for i, x in counter.items():
                    if x:
                        res |= (1 << i)
                return res
            res = 0
            right = start
            add(nums[start])
            # 以下使用双指针
            for left in range(start, end):
                cur = trans()
                if right < left:
                    right = left
                    add(nums[left])
                    cur = nums[left]
                while right < end and cur & nums[right] != k:
                    add(nums[right])
                    right += 1
                if right == end:
                    break
                res += end - right
                remove(nums[left])
            return res

        for i in range(len(div) - 1):
            ans += calc(div[i] + 1, div[i + 1])

        return ans

so = Solution()
print(so.countSubarrays(nums = [1,1,2], k = 1))
print(so.countSubarrays(nums = [1,1,1], k = 1))
print(so.countSubarrays(nums = [1,2,3], k = 2))




