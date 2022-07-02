class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        l1 = []
        l2 = []
        for i in nums[1:]:
            if i <= nums[0]:
                l1.append(i)
            else:
                l2.append(i)
        return self.sortArray(l1) + [nums[0]] + self.sortArray(l2)

so = Solution()
print(so.sortArray([5,2,3,1]))
print(so.sortArray([5,1,1,2,0,0]))