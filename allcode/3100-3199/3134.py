

from leetcode.allcode.competition.mypackage import *

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        N = n * (n + 1) // 2  # 非空子数组个数
        def check(val):
            # 检查不同元素个数<=val的子数组个数是否>= (N + 1) // 2
            # 最小满足这个函数的数，就是答案
            r = 0
            s = {}
            res = 0
            for l in range(n):
                while r < n and len(s) <= val:
                    if nums[r] in s:
                        s[nums[r]] += 1
                    else:
                        s[nums[r]] = 1
                    r += 1
                if len(s) > val:
                    res += (r - l - 1)
                else:
                    res += (r - l)
                if s[nums[l]] == 1:
                    del(s[nums[l]])
                else:
                    s[nums[l]] -= 1

            return res >= (N + 1) // 2

        lo, hi = 1, len(set(nums))
        if check(lo): return lo
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi



so = Solution()
print(so.medianOfUniquenessArray(nums = [91,64,76,18,61,55,46,93,65,99]))
print(so.medianOfUniquenessArray(nums = [3,4,3,4,5]))
print(so.medianOfUniquenessArray(nums = [1,2,3]))




