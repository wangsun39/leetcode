

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @cache
        def dfs(idx, o1, o2):  # 前idx个数，经过若干操作后，剩余操作1 o1 次，操作2 o2 次时，最小和
            if idx == n:
                return 0

            res = dfs(idx + 1, o1, o2) + nums[idx]
            if o2 and nums[idx] >= k:
                res = min(res, dfs(idx + 1, o1, o2 - 1) + nums[idx] - k)
                if o1:
                    res = min(res, dfs(idx + 1, o1 - 1, o2 - 1) + (nums[idx] - k + 1) // 2)
            if o1:
                res = min(res, dfs(idx + 1, o1 - 1, o2) + (nums[idx] + 1) // 2)
                if (nums[idx] + 1) // 2 >= k and o2:
                    res = min(res, dfs(idx + 1, o1 - 1, o2 - 1) + (nums[idx] + 1) // 2 - k)
            return res

        return dfs(0, op1, op2)



so = Solution()
print(so.minArraySum(nums = [376,404,771,503,483,538], k = 452, op1 = 4, op2 = 2))
print(so.minArraySum(nums = [307,624,329,684,851,317,205], k = 431, op1 = 7, op2 = 1))
print(so.minArraySum(nums = [882,307,624,469,329,684,851,608,317,205], k = 431, op1 = 9, op2 = 4))
print(so.minArraySum(nums = [2,10,9,0,4], k = 3, op1 = 5, op2 = 2))
print(so.minArraySum(nums = [9], k = 5, op1 = 1, op2 = 1))
print(so.minArraySum(nums = [2,4,3], k = 3, op1 = 2, op2 = 1))
print(so.minArraySum(nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1))




