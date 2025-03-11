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
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        div = []
        n = len(nums)
        for i, x in enumerate(nums):
            if x & k != k:  # 任何子数组都不会包含这种 x
                div.append(i)
        if not div or div[0] > 0:
            div.insert(0, -1)
        div.append(n)
        counter = [[0] * 32]  # counter[i][j] 前i项的按位累计和(前缀和)
        for x in nums:
            i = 0
            count = counter[-1][:]
            while x:
                if x & 1:
                    count[i] += 1
                i += 1
                x >>= 1
            counter.append(count)
        ans = 0
        def calc(start, end):   # 计算 [start, end) 区间内的子数组个数
            res = 0
            right = start

            def trans():
                len = right - left
                count = [counter[right][i] - counter[left][i] for i in range(32)]
                res = 0
                for i, x in enumerate(count):
                    if x and x == len:
                        res |= (1 << i)
                return res

            for left in range(start, end):  # 双指针
                right = max(right, left + 1)
                left_x = nums[left]
                if left_x == k:
                    res += end - left
                    continue
                while right <= end and trans() != k:
                    right += 1
                if right > end:
                    break
                res += end - right + 1
            return res


        for i in range(len(div) - 1):
            ans += calc(div[i] + 1, div[i + 1])

        return ans
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter()
        def add(x):
            i = 0
            while x:
                if x & 1:
                    counter[i] += 1
                i += 1
        def sub(x):
            i = 0
            while x:
                if x & 1:
                    counter[i] -= 1
                i += 1
        def to_num():
            res = 0
            for k, v in counter.items():
                if v: res |= (1 << k)
            return res

        l, r = 0, -1
        ans = 0
        while l < n:
            while r < n:
                add(nums[r])
                v = to_num()
                av = v & k
                if av != k:
                    l = r + 1
                    counter.clear()
                elif v > k:
                    r += 1
                else:
                    ans += 1
        return ans


so = Solution()
print(so.countSubarrays(nums = [9,1,8,9,5], k = 0))  # 7
print(so.countSubarrays(nums = [1,2,3], k = 2))  # 2
print(so.countSubarrays(nums = [1,9,9,7,4], k = 1))  # 6
print(so.countSubarrays(nums = [3,5,5,3,10], k = 0))  # 3
print(so.countSubarrays(nums = [2,1,2,4,0], k = 0))  # 11
print(so.countSubarrays(nums = [1,1,1], k = 1))  # 6
print(so.countSubarrays(nums = [1,1,2], k = 1))  # 3




