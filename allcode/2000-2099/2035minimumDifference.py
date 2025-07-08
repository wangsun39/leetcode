# 给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。nums 中每个元素都需要放入两个数组之一。
#
# 请你返回 最小 的数组和之差。
#
#
#
# 示例 1：
#
# example-1
#
# 输入：nums = [3,9,7,3]
# 输出：2
# 解释：最优分组方案是分成 [3,9] 和 [7,3] 。
# 数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
# 示例 2：
#
# 输入：nums = [-36,36]
# 输出：72
# 解释：最优分组方案是分成 [-36] 和 [36] 。
# 数组和之差的绝对值为 abs((-36) - (36)) = 72 。
# 示例 3：
#
# example-3
#
# 输入：nums = [2,-1,0,4,-2,-9]
# 输出：0
# 解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
# 数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
#
#
# 提示：
#
# 1 <= n <= 15
# nums.length == 2 * n
# -107 <= nums[i] <= 107

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2

        def calc(arr):  # 将arr中的数分成两组，用一组的和减另一组的和，将所有的差值放入一个哈希表内
            m = len(arr)
            s = sum(arr)
            ds = defaultdict(set)
            for i in range(1 << m):
                su = 0  # 数字 i 对于的bitmap的和
                for j in range(m):
                    if i & (1 << j):
                        su += arr[j]
                ds[i.bit_count()].add(su - (s - su))
            dl = defaultdict(list)
            for k in ds:
                dl[k] = sorted(list(ds[k]))
            return dl

        dl1 = calc(nums[:n])
        dl2 = calc(nums[n:])
        ans = inf
        for k, arr1 in dl1.items():
            for x in arr1:
                p = bisect_left(dl2[n - k], -x)
                if p:
                    ans = min(ans, abs(dl2[n - k][p - 1] + x))
                if p < len(dl2[n - k]):
                    ans = min(ans, abs(dl2[n - k][p] + x))

        return ans


so = Solution()
print(so.minimumDifference([3,9,7,3]))


