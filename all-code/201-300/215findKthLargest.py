class Solution:
    def findKthLargest1(self, nums, k: int) -> int:
        max_num = len(nums)
        if max_num <= 2:
            return max(nums) if k == 1 else min(nums)
        large_set = []
        small_set = []
        for i in range(1, max_num):
            if nums[i] > nums[0]:
                large_set.append(nums[i])
            else:
                small_set.append(nums[i])
        large_num = len(large_set)
        if large_num >= k:
            return self.findKthLargest1(large_set, k)
        elif large_num == k - 1:
            return nums[0]
        else:
            return self.findKthLargest1(small_set, k - large_num - 1)

    def findKthLargest(self, nums, k: int) -> int:
        max_num = len(nums)
        if max_num <= 2:
            return max(nums) if k == 1 else min(nums)
        large_set = []
        small_set = []
        # 每轮递归选取一个基准的值nums_c，使得small中的值都比nums_c小，large中的值都比nums_c大
        # nums_c选取的方法，从列表头或列表尾获取（最好能随机，防止large和small的数量差距太多，造成递归次数很多，性能下降）
        if max_num % 2 == 1:
            nums_c, start_i, end_i = nums[0], 1, max_num
        else:
            nums_c, start_i, end_i = nums[-1], 0, max_num-1
        for i in range(start_i, end_i):
            if nums[i] > nums_c:
                large_set.append(nums[i])
            else:
                small_set.append(nums[i])
        large_num = len(large_set)
        if large_num >= k:
            return self.findKthLargest(large_set, k)
        elif large_num == k - 1:
            return nums_c
        else:
            return self.findKthLargest(small_set, k - large_num - 1)

so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.findKthLargest([1,2,3,4,5,6], 1))

