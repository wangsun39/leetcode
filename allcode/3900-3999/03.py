

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter()
        for a, b in pairwise(nums):
            counter[b - a] += 1
        if counter[1] == n - 1:
            return 0
        if counter[-1] == n - 1:
            return 1
        if counter[1] == n - 2 and counter[1 - n] == 1:
            for i in range(n):
                if nums[i] == 0:
                    return min(i, n - i + 2)
        if counter[-1] == n - 2 and counter[n - 1] == 1:
            for i in range(n):
                if nums[i] == n - 1:
                    return min(i + 1, n - i + 1)
        return -1




so = Solution()
print(so.minOperations([2,0,1,3]))
print(so.minOperations([2,1,0]))
print(so.minOperations([2,3,4,5,6,0,1]))  # 2
print(so.minOperations([1,0,2]))  # 2
print(so.minOperations([0,2,1]))




