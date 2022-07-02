import bisect
class Solution:
    def relativeSortArray(self, arr1, arr2):
        d = {}
        remain = []
        res = []
        for i in arr2:
            d[i] = 0
        for i in arr1:
            if i in d:
                d[i] += 1
            else:
                bisect.insort(remain, i)
        for i in arr2:
            for j in range(d[i]):
                res.append(i)
        return res + remain




obj = Solution()
print(obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))

