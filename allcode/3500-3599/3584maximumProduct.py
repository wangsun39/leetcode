

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if m == 1:
            return max(x * x for x in nums)
        if n == 2:
            return nums[0] * nums[1]
        if m == n:
            return nums[0] * nums[-1]
        mn = mx = None
        mn1 = mx1 = None
        zero = None
        ans = -inf
        for r in range(m - 1, n):
            l = r - m + 1
            if nums[l] > 0:
                if mn1 is None:
                    mn1 = mx1 = nums[l]
                else:
                    mx1 = max(mx1, nums[l])
                    mn1 = min(mn1, nums[l])
            elif nums[l] < 0:
                if mn is None:
                    mn = mx = nums[l]
                else:
                    mx = max(mx, nums[l])
                    mn = min(mn, nums[l])
            else:
                zero = 1
            x = nums[r]
            if x == 0:
                ans = max(ans, 0)
            elif x > 0:
                if mx1 is not None:
                    ans = max(ans, mx1 * x)
                elif zero is not None:
                    ans = max(ans, 0)
                else:
                    ans = max(ans, x * mx)
            else:
                if mx is not None:
                    ans = max(ans, mn * x)
                elif zero is not None:
                    ans = max(ans, 0)
                else:
                    ans = max(ans, x * mn1)
        return ans



so = Solution()
print(so.maximumProduct(nums = [2,3,4,-10,-5,-3], m = 4))  # -6
print(so.maximumProduct(nums = [1,3,4,-5], m = 4))  # -5
print(so.maximumProduct(nums = [-1,-9,2,3,-2,-3,1], m = 1))




