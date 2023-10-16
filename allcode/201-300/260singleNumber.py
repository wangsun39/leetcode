from functools import reduce
from typing import List


class Solution:
    def singleNumber1(self, nums):
        d = {}
        r = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for k in d:
            if d[k] == 1:
                r.append(k)
        return r

    def singleNumber(self, nums: List[int]) -> List[int]:
        v = reduce(lambda x, y: x ^ y, nums)
        l = v & -v
        v1 = v2 = 0
        for x in nums:
            if x & l:
                v1 ^= x
            else:
                v2 ^= x
        return [v1, v2]



so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.singleNumber([1,2,1,3,2,5]))

