from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        first_idx, first_val = 0, nums[0]
        curMaxSum = sum(nums[:k])
        nextSum = curMaxSum
        for i in range(k, N):
            nextSum = nextSum - first_val + nums[i]
            curMaxSum = max(nextSum, curMaxSum)
            first_idx += 1
            first_val = nums[first_idx]

        return curMaxSum / k


so = Solution()
print(so.findMaxAverage([0,4,0,3,2], 1))
print(so.findMaxAverage([1,12,-5,-6,50,3], 4))

