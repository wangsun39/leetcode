class Solution:
    def findLengthOfLCIS(self, nums):
        num = len(nums)
        if num <= 1:
            return num
        res = 1
        start, pre = [0, nums[0]], [0, nums[0]]
        for idx, cur in enumerate(nums):
            if cur <= pre[1]:
                start, pre = [idx, cur], [idx, cur]
            else:
                res = max(res, idx-start[0]+1)
                pre = [idx, cur]
        return res


obj = Solution()
print(obj.findLengthOfLCIS([1,3,5,4,7]))
print(obj.findLengthOfLCIS([2,2,2,2,2]))
