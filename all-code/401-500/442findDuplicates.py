class Solution:
    def findDuplicates(self, nums):
        num = len(nums)
        dup = []
        for i in range(num):
            if i+1 == nums[i]:
                continue
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        print(nums)
        for i in range(num):
            if i+1 != nums[i]:
                dup.append(nums[i])
        return dup




so = Solution()
print(so.findDuplicates([4,3,2,7,8,2,3,1]))
#print(so.diffWaysToCompute("2*3-4*5"))

