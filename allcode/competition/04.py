

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)

        dd = [{} for _ in range(n)]
        counter = [[0] * 16 for _ in range(n)]
        for i in range(n):
            x = nums[i]
            # dd[i][x] = i
            bit = 0
            if i > 0:
                counter[i] = counter[i - 1][:]
            while x:
                if x & 1:
                    counter[i][bit] += 1
                x >>= 1
                bit += 1
        print(counter)


        @cache
        def dfs(a, b):  # 从第a个数开始，划分b个子数组，得到的最小子数组值之和
            if a == n:
                if b > 0:
                    return inf
                else:
                    return 0
            res = inf
            AND = nums[a]
            for i in range(a, n):
                AND &= nums[i]
                if AND == andValues[m - b]:
                    res = min(res, nums[i] + dfs(i + 1, b - 1))
            return res

        ans = dfs(0, m)
        return ans if ans < inf else -1





so = Solution()
print(so.minimumValueSum(nums = [1,4,3,3,2], andValues = [0,3,3,2]))
print(so.minimumValueSum(nums = [2,3,5,7,7,7,5], andValues = [0,7,5]))
print(so.minimumValueSum(nums = [1,2,3,4], andValues = [2]))




