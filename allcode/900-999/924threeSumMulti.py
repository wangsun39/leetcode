# 给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。
#
# 由于结果会非常大，请返回 109 + 7 的模。
#
#
#
# 示例 1：
#
# 输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举(arr[i], arr[j], arr[k])：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
# 示例 2：
#
# 输入：arr = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
#
#
# 提示：
#
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300

from leetcode.allcode.competition.mypackage import *

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        counter = [[0] * (target + 1) for _ in range(n)]  # counter[i][j] 表示从arr[i]开始向后有多少个值为j的数字
        if arr[n - 1] <= target:
            counter[n - 1][arr[n - 1]] = 1
        for i in range(n - 2, -1, -1):
            counter[i] = counter[i + 1][:]
            if arr[i] <= target:
                counter[i][arr[i]] += 1
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                s1 = arr[i] + arr[j]
                s2 = target - s1
                if s2 >= 0:
                    ans += counter[j + 1][s2]
                    ans %= MOD
        return ans



so = Solution()
print(so.threeSumMulti([1,0,1,0,2,1,2], 1))
print(so.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
print(so.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))




