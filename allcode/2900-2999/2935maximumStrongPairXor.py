

from leetcode.allcode.competition.mypackage import *



class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mx = max(nums)
        prefix = 0
        ans = 0
        for i in range(mx.bit_length() - 1, -1, -1):
            prefix |= (1 << i)
            s = set()  # hash 表
            right = 0
            for j, x in enumerate(nums):
                while right < n and nums[right] <= x * 2:
                    s.add(nums[right] & prefix)
                    right += 1
                t = ans | (1 << i)
                if t ^ (x & prefix) in s:
                    ans |= (1 << i)
                    break
                if x & prefix in s:
                    s.remove(x & prefix)
        return ans




so = Solution()
print(so.maximumStrongPairXor([1,2,2,1,2]))
print(so.maximumStrongPairXor([1,2,3,4,5]))
print(so.maximumStrongPairXor([10,100]))
print(so.maximumStrongPairXor([5,6,25,30]))




