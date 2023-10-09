class Solution:
    def singleNumber(self, nums):
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




so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.singleNumber([1,2,1,3,2,5]))

