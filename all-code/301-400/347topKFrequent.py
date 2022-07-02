class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = []
        for i in range(0, 20000):
            c.append([])
        for key, value in d.items():
            c[value].append(key)
        r = []
        num = 0
        for i in range(20000-1, -1, -1):
            if len(c[i]) > 0:
                r = r + c[i]
                num += len(c[i])
                if num >= k:
                    return r



so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.topKFrequent([1,1,1,2,2,3], 2))




