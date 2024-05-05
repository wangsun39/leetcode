from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def getSectionMax(arr):
            max_prefix = 0
            max_sum, tmp_sum, total_sum = -99999, 0, 0
            for idx, e in enumerate(arr):
                tmp_sum += e
                total_sum += e
                max_prefix = max(total_sum, max_prefix)
                if max_sum < tmp_sum:
                    max_sum = tmp_sum
                if tmp_sum < 0:
                    tmp_sum = 0
            max_suffix = tmp_sum
            return max_sum, total_sum, max_prefix, max_suffix

        max_sum, total_sum, left_max, right_max = getSectionMax(arr)
        if 1 == k:
            return max_sum
        second_max_sum = total_sum * (k - 2) + left_max + right_max
        third_max_sum = left_max + right_max
        return max(max_sum, second_max_sum, third_max_sum, 0) % (10**9+7)


obj = Solution()
#print(obj.kConcatenationMaxSum([1,-2], 3))
print(obj.kConcatenationMaxSum([-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3], 6))
print(obj.kConcatenationMaxSum([-12,-1,-4,11,-8,6,9,-5,-7,7,12,10], 10))
print(obj.kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5))
print(obj.kConcatenationMaxSum([3,5,-6,-9,10,5], 3))
print(obj.kConcatenationMaxSum([1,-2,1], 5))
print(obj.kConcatenationMaxSum([-1,-2], 7))

