# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
#  
#
# 示例：
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#  
#
# 提示：
#
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


from collections import defaultdict
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def find(l, x):  # l 是排序的列表，返回x可以插入的最小下标
            N = len(l)
            if x <= l[0]:
                return 0
            if x > l[N - 1]:
                return N
            low, high = 0, N - 1
            while low < high - 1:
                mid = (low + high) // 2
                if x > l[mid]:
                    low = mid
                else:
                    high = mid
            return high
        def findLessNum(l, x):  # l 是排序的列表，返回比x小的元素个数
            return find(l, x)
        if 0 == len(nums): return []
        if 1 == len(nums): return [0]
        res = [0]
        l = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            e = findLessNum(l, nums[i])
            res.insert(0, e)
            l = l[:e] + [nums[i]] + l[e:]
        return res



so = Solution()
print(so.countSmaller([]))
print(so.countSmaller([5,2,6,1]))

