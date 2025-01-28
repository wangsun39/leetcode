# 给你一个正整数数组nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
#
# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
# 示例 2：
#
# 输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
#
#
# 提示：
#
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 105

from typing import List
from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        dic1 = defaultdict(int)  # num: num出现的次数
        dic2 = defaultdict(int)  # 出现的次数k: 多少个num出现k次
        for i, e in enumerate(nums):
            dic1[e] += 1
            dic2[dic1[e]] += 1
            if dic1[e] - 1 in dic2:
                dic2[dic1[e] - 1] -= 1
                if dic2[dic1[e] - 1] == 0:
                    del(dic2[dic1[e] - 1])
            if len(dic2) == 1 and list(dic2.keys())[0] == 1:
                ans = i + 1
            elif len(dic2) == 2:
                if 1 in dic2.keys() and dic2[1] == 1:
                    ans = i + 1
                l = list(dic2.keys())
                l.sort()
                if l[1] - l[0] == 1 and dic2[l[1]] == 1:
                    ans = i + 1
            elif len(dic1) == 1:
                ans = i + 1
        return max(ans, 2)





obj = Solution()
print(obj.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))  # 8
print(obj.maxEqualFreq([1,1,1,2,2,2]))  # 5
print(obj.maxEqualFreq([1,1,1,2,2,2,3,3,3]))  # 7
print(obj.maxEqualFreq([1,1,1,1,1,1]))  # 6
print(obj.maxEqualFreq([1,1]))  # 2
print(obj.maxEqualFreq([1,2,3,4,5,6,7,8,9]))  # 9
print(obj.maxEqualFreq([1,2]))  # 2
print(obj.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))  # 13
print(obj.maxEqualFreq([2,2,1,1,5,3,3,5]))  # 7

