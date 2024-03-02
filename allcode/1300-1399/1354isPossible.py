# 给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：
#
# 令 x 为你数组里所有元素的和
# 选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
# 你可以重复该过程任意次
# 如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。
#
#
#
# 示例 1：
#
# 输入：target = [9,3,5]
# 输出：true
# 解释：从 [1, 1, 1] 开始
# [1, 1, 1], 和为 3 ，选择下标 1
# [1, 3, 1], 和为 5， 选择下标 2
# [1, 3, 5], 和为 9， 选择下标 0
# [9, 3, 5] 完成
# 示例 2：
#
# 输入：target = [1,1,1,2]
# 输出：false
# 解释：不可能从 [1,1,1,1] 出发构造目标数组。
# 示例 3：
#
# 输入：target = [8,5]
# 输出：true
#
#
# 提示：
#
# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        s = sum(target)
        target = SortedList(target)
        # 倒序考虑变换过程  下面注释的代码性能不够，思路是对的，下面改进了递推的速度
        # while target[-1] > 1:
        #     pre_s = mx = target[-1]  # 上一轮的和
        #     left_s = s - mx  # 这一轮除了最大值之外的元素和
        #     orig = pre_s - left_s  # mx 在上一轮的值
        #     if orig <= 0:
        #         return False
        #     s -= (mx - orig)
        #     target.pop(-1)
        #     target.add(orig)
        while target[-1] > 1:
            mx = target[-1]  # 上一轮的和
            left_s = s - mx  # 这一轮除了最大值之外的元素和
            # orig = mx - left_s  当left_s远小于mx时，可以多次递推，orig = mx - m * left_s, 设orig 为left_s，即递推m步到达<=left_s
            m = max(mx // left_s - 1, 1)   # 一次递推多部，直到 mx< left_s
            orig = mx - m * left_s  # mx 在上一轮的值
            if orig <= 0:
                return False
            s -= (mx - orig)
            target.pop(-1)
            target.add(orig)
        return True



so = Solution()
print(so.isPossible([2]))
print(so.isPossible([1,1000000000]))
print(so.isPossible([9,3,5]))
print(so.isPossible([1,1,1,2]))
print(so.isPossible([8,5]))




