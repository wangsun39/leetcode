

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        if n == 1: return 0
        if n == 2:
            return abs(nums[0] - nums[1]) * cost1 % MOD
        mx = max(nums)
        if cost1 * 2 <= cost2:
            ans = 0
            for x in nums:
                ans += (mx - x) * cost1
                ans %= MOD
            return ans
        hp = nums[:]
        heapify(hp)
        ans = 0
        while True:
            x = heappop(hp)
            y = heappop(hp)
            if x == y == mx:
                return ans
            if y == mx:
                heappush(hp, x)
                heappush(hp, y)
                break
            heappush(hp, x + (mx - y))
            heappush(hp, mx)
            ans += cost2 * (mx - y)
            ans %= MOD
            # z = heappop(hp)
            # ans += (z - y) * cost2
            # heappush(hp, x + z - y)
            # heappush(hp, z)
            # heappush(hp, z)
        m = mx - hp[0]
        i = 0
        mn = inf
        flg = 0
        while True:
            v = i * n + m
            if i * (n - 1) >= m + i:
                flg += 1
                if v & 1 == 0:
                    mn = min(mn, v // 2 * cost2)
                else:
                    mn = min(mn, v // 2 * cost2 + cost1)
                if flg >= 2:
                    break
                i += 1
            else:
                mn = min(mn, i * (n - 1) * cost2 + (m + i - i * (n - 1)) * cost1)
                i += 1
            mn %= MOD
        ans += mn
        ans %= MOD
        return ans


so = Solution()
print(so.minCostToEqualizeArray([4,3,1,8],5,1))
print(so.minCostToEqualizeArray([1,1000000],
1000000,
1))
print(so.minCostToEqualizeArray([60,19,53,31,57],60,2))
print(so.minCostToEqualizeArray([1,14,14,15],2,1))
print(so.minCostToEqualizeArray(nums = [2,3,3,3,5], cost1 = 2, cost2 = 1))
print(so.minCostToEqualizeArray(nums = [3,5,3], cost1 = 1, cost2 = 3))
print(so.minCostToEqualizeArray(nums = [4,1], cost1 = 5, cost2 = 2))




