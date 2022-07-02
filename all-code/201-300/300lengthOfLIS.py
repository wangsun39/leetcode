import math
class Solution:
    def lengthOfLIS(self, nums):
        number = len(nums)
        if number == 0:
            return 0
        A = [0] * number
        A[0] = 1
        # A[i] 表示以nums[i]结尾的最大字序长度
        for i in range(1, number):
            if nums[i] == nums[i-1]:
                A[i] = A[i-1]
            else:
                max_v = 1
                for j in range(i):
                    #print(max_v, i, j)
                    if nums[i] > nums[j]:
                        max_v = max(max_v, A[j]+1)
                A[i] = max_v
        print(A)
        return max(A)




so = Solution()
print(so.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(so.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

