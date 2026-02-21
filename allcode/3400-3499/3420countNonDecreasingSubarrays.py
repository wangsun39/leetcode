# 给你一个长度为 n 的数组 nums 和一个整数 k 。
#
# 对于 nums 中的每一个子数组，你可以对它进行 至多 k 次操作。每次操作中，你可以将子数组中的任意一个元素增加 1 。
#
# 注意 ，每个子数组都是独立的，也就是说你对一个子数组的修改不会保留到另一个子数组中。
#
# 请你返回最多 k 次操作以内，有多少个子数组可以变成 非递减 的。
#
# 如果一个数组中的每一个元素都大于等于前一个元素（如果前一个元素存在），那么我们称这个数组是 非递减 的。
#
#
#
# 示例 1：
#
# 输入：nums = [6,3,1,2,4,4], k = 7
#
# 输出：17
#
# 解释：
#
# nums 的所有 21 个子数组中，只有子数组 [6, 3, 1] ，[6, 3, 1, 2] ，[6, 3, 1, 2, 4] 和 [6, 3, 1, 2, 4, 4] 无法在 k = 7 次操作以内变为非递减的。所以非递减子数组的数目为 21 - 4 = 17 。
#
# 示例 2：
#
# 输入：nums = [6,3,1,3,6], k = 4
#
# 输出：12
#
# 解释：
#
# 子数组 [3, 1, 3, 6] 和 nums 中所有小于等于三个元素的子数组中，除了 [6, 3, 1] 以外，都可以在 k 次操作以内变为非递减子数组。总共有 5 个包含单个元素的子数组，4 个包含两个元素的子数组，除 [6, 3, 1] 以外有 2 个包含三个元素的子数组，所以总共有 1 + 5 + 4 + 2 = 12 个子数组可以变为非递减的。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        g = defaultdict(list)
        n = len(nums)
        stack = []  # 单调减的栈，记录左侧第一个比nums[i]大的位置
        pos_r = [n] * n  # 右侧第一个>=nums[i]的位置
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] <= x:
                pos_r[stack.pop()] = i
            if stack:
                g[stack[-1]].append(i)
            stack.append(i)

        l = 0  # 滑窗左端点
        cnt = 0  # 滑窗内元素需要操作的次数
        dq = deque()  # 在滑窗的过程中，用单调减队列记录滑窗中的最大值元素
        ans = 0
        for r, x in enumerate(nums):  # 枚举滑窗右端点
            while dq and nums[dq[-1]] < x:
                dq.pop()
            dq.append(r)
            cnt += nums[dq[0]] - x
            while cnt > k:  # 窗口内操作次数过大，需要右移左端点
                for y in g[l]:  # 枚举每个l的子节点，每个子节点对应的子树都要减少一个统一数值
                    if y > r:
                        break
                    cnt -= (nums[l] - nums[y]) * (min(pos_r[y], r + 1) - y)  # 子树的大小 (nums[l] - nums[y])
                l += 1
                if l > r: break

            while l > dq[0]:
                dq.popleft()

            ans += r - l + 1

        return ans




so = Solution()
print(so.countNonDecreasingSubarrays(nums = [24,25,25,8,4], k = 7))  # 9
print(so.countNonDecreasingSubarrays(nums = [6,3,1,2,4,4], k = 7))




