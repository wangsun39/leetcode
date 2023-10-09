class Solution:
    def findPeakElement(self, nums):
        if 1 == len(nums):
            return 0
        if 2 == len(nums):
            return 0 if nums[0] > nums[1] else 1
        left, right = 0, len(nums) - 1
        while right - left >= 2:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                right = mid - 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        if right == left:
            return left
        return left if nums[left] > nums[right] else right


so = Solution()
# print(so.compareVersion('1.1.2', '1.1.1'))
# print(so.compareVersion("7.5.2.4", "7.5.3"))
print(so.findPeakElement([1, 2, 3, 1]))
print(so.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
