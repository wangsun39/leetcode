# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。
#
# 实现 Solution class:
#
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#
#
# 示例 1：
#
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
#
#
# 提示：
#
# 1 <= nums.length <= 50
# -106 <= nums[i] <= 106
# nums 中的所有元素都是 唯一的
# 最多可以调用 104 次 reset 和 shuffle

from leetcode.allcode.competition.mypackage import *

class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]


    def reset(self) -> List[int]:
        return self.orig


    def shuffle(self) -> List[int]:
        tmp = self.orig[:]
        n = len(self.orig)
        nums = [0] * n
        for i in range(n, 0, -1):
            idx = random.randint(1, i) - 1
            nums[i - 1] = tmp[idx]
            tmp[idx], tmp[i - 1] = tmp[i - 1], tmp[idx]
        return nums



so = Solution([1,2,3])
print(so.shuffle())
print(so.shuffle())
print(so.shuffle())
print(so.shuffle())
print(so.shuffle())




