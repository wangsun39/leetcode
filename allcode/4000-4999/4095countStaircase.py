# 给你一个整数数组 nums。
#
# 考虑一个子数组中的所有不同值，并按它们首次出现的顺序排列。
#
# 如果其中有 k 个不同值，且第一个不同值恰好出现一次，第二个不同值恰好出现两次，以此类推，第 k 个不同值恰好出现 k 次，则称该子数组为频次阶梯。
#
# 即，按首次出现的顺序排列的各个不同值，其出现次数必须恰好为 1, 2, 3, ..., k。
#
# 返回 nums 中频次阶梯子数组的数量。
#
# 子数组是数组中一段连续且非空的元素序列。
#
# 一个值在子数组中的频次，是指它在该子数组中出现的次数。
#
#
#
# 示例 1：
#
# 输入： nums = [5,8,8,2,2,2]
#
# 输出： 9
#
# 解释：
#
# 每个单元素子数组的频次序列都是 [1]，这样的子数组共有 6 个。另外还有 3 个更长的子数组符合条件：
#
# 子数组	按首次出现顺序排列的值	频次
# nums[0...2] = [5, 8, 8]	先 5，后 8	[1, 2]
# nums[2...4] = [8, 2, 2]	先 8，后 2	[1, 2]
# nums[0...5] = [5, 8, 8, 2, 2, 2]	依次为 5、8、2	[1, 2, 3]
# 因此，答案为 6 + 3 = 9。
#
# 示例 2：
#
# 输入： nums = [6,6,9,9]
#
# 输出： 5
#
# 解释：
#
# 每个单元素子数组的频次序列都是 [1]，这样的子数组共有 4 个。另外还有 1 个更长的子数组符合条件：
#
# 子数组	按首次出现顺序排列的值	频次
# nums[1...3] = [6, 9, 9]	先 6，后 9	[1, 2]
# 因此，答案为 4 + 1 = 5。
#
# 示例 3：
#
# 输入： nums = [2,3,4,4,3,4]
#
# 输出： 8
#
# 解释：
#
# 每个单元素子数组的频次序列都是 [1]，这样的子数组共有 6 个。另外还有 2 个更长的子数组符合条件：
#
# 子数组	按首次出现顺序排列的值	频次
# nums[1...3] = [3, 4, 4]	先 3，后 4	[1, 2]
# nums[0...5] = [2, 3, 4, 4, 3, 4]	依次为 2、3、4	[1, 2, 3]
# 因此，答案为 6 + 2 = 8。
#
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ps = defaultdict(deque)  # 每个元素的位置列表
        for i, x in enumerate(nums):
            ps[x].append(i)
        sl = SortedList()
        for key, dq in ps.items():
            sl.add([dq[0], key])
        ans = 0
        for i in range(n):
            # 枚举子数组的左端点
            y = nums[i]
            m = len(sl)  # 子数组中可能的最多不同元素个数
            if len(ps[y]) == 1:
                right = n - 1  # 子数组的最大右端点
            else:
                right = ps[y][1] - 1
            left = i  # 子数组的最小右端点
            for j in range(m):
                x = sl[j][1]  # 个数为 j + 1 的元素
                if len(ps[x]) < j + 1:
                    # x 的个数不足 j 个，结束搜索
                    break
                if ps[x][j] > right:
                    break
                left = MAX(left, ps[x][j])
                if left - i + 1 == (1 + j + 1) * (j + 1) // 2:
                    # 在区间 [i, left] 之间的子数组，元素个数为是否 == 1+2+...+j+1
                    # 相同则表示这个区间内没有其他元素
                    ans += 1
                if len(ps[x]) > j + 1:
                    right = MIN(right, ps[x][j + 1] - 1)
            ps[y].popleft()
            sl.remove([i, y])
            if len(ps[y]):
                sl.add([ps[y][0], y])

        return ans



so = Solution()
print(so.countStaircase(nums = [2,3,4,4,3,4]))
print(so.countStaircase(nums = [5,8,8,2,2,2]))
print(so.countStaircase(nums = [5,8,2,8,2,2]))
print(so.countStaircase(nums = [6,6,9,9]))



