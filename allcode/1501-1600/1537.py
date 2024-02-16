

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        MOD = 10 ** 9 + 7
        d1 = {v: k for k, v in enumerate(nums1)}
        d2 = {v: k for k, v in enumerate(nums2)}

        @cache
        def dfs(idx, idy, jump): # idx 表示在nums1还是在nums2上，idy表示当前的下标，返回最大和
            if idx == 0:
                if idy == n1:
                    return 0
                x = nums1[idy]
                r1 = dfs(idx, idy + 1, False)
                if not jump:
                    r1 += x
                r2 = 0
                if not jump and x in d2:
                    r2 = dfs(1 - idx, d2[x], True) + x
                return max(r1, r2)
            else:
                if idy == n2:
                    return 0
                x = nums2[idy]
                r1 = dfs(idx, idy + 1, False)
                if not jump:
                    r1 += x
                r2 = 0
                if not jump and x in d1:
                    r2 = dfs(1 - idx, d1[x], True) + x
                return max(r1, r2)
        return max(dfs(0, 0, False), dfs(1, 0, False)) % MOD

so = Solution()
print(so.maxSum([6,7,12,13,14,17,20], [1,4,5,7]))
print(so.maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]))
print(so.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))
print(so.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))




