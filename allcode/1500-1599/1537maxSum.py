

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        MOD = 10 ** 9 + 7
        d1 = {v: k for k, v in enumerate(nums1)}
        d2 = {v: k for k, v in enumerate(nums2)}

        @cache
        def dfs(in_nums1, idx, jump): # idx 表示当前是否在在nums1上，idy表示当前的下标，返回最大和
            if in_nums1:
                if idx == n1:
                    return 0
                x = nums1[idx]
                r1 = dfs(in_nums1, idx + 1, False)
                if not jump:
                    r1 += x
                r2 = 0
                if not jump and x in d2:
                    r2 = dfs(not in_nums1, d2[x], True) + x
                return max(r1, r2)
            else:
                if idx == n2:
                    return 0
                x = nums2[idx]
                r1 = dfs(in_nums1, idx + 1, False)
                if not jump:
                    r1 += x
                r2 = 0
                if not jump and x in d1:
                    r2 = dfs(not in_nums1, d1[x], True) + x
                return max(r1, r2)
        return max(dfs(True, 0, False), dfs(False, 0, False)) % MOD

so = Solution()
print(so.maxSum([6,7,12,13,14,17,20], [1,4,5,7]))
print(so.maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]))
print(so.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))
print(so.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))




