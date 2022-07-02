# 给你一个数组 nums ，请你完成两类查询。
#
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
#  
#
# 示例 1：
#
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#  
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 104 


from typing import List
from collections import defaultdict


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.partialSum = [0] * self.N
        self.partialSum[0] = self.nums[0]
        for i in range(1, self.N):
            self.partialSum[i] = self.partialSum[i - 1] + nums[i]

        self.minus = [0] * self.N
        self.minus[0] = self.partialSum[0]
        for i in range(1, self.N):
            self.minus[i] = self.partialSum[i] - self.partialSum[i - 1]


    def update(self, index: int, val: int) -> None:
        old = self.nums[index]
        self.nums[index] = val
        self.minus[index] += (val - old)

    def sumRange(self, left: int, right: int) -> int:



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


so = NumArray()
print(so.maxProfit([1,2,3,0,2]))
print(so.maxProfit([5,7,11,13,17,19,29,43,47,53]))

