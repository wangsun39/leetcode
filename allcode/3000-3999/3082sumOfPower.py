

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        d = {}

        # @cache
        def dfs(start, target):
            if (start, target) in d:
                return d[(start, target)]
            if target < 0:
                d[(start, target)] = []
                return []
            if target == 0:
                d[(start, target)] = [0]
                return [0]
            if start == n - 1:
                if target == nums[-1]:
                    d[(start, target)] = [1]
                    return [1]
                else:
                    d[(start, target)] = []
                    return []
            r1 = dfs(start + 1, target)
            r2 = dfs(start + 1, target - nums[start])
            for i in range(len(r2)):
                r2[i] += 1
            # print(start, target, r1 + r2)
            d[(start, target)] = r1 + r2
            return r1 + r2

        sub = dfs(0, k)
        ans = 0
        for x in sub:
            ans += pow(2, n - x, MOD)
            ans %= MOD
        return ans



so = Solution()
print(so.sumOfPower([2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
49))
print(so.sumOfPower([1,1,2,3,3], 5))
print(so.sumOfPower(nums = [5,5,6], k = 5))
print(so.sumOfPower(nums = [1,2,3], k = 3))
print(so.sumOfPower(nums = [2,3,3], k = 5))
print(so.sumOfPower(nums = [1,2,3], k = 7))




