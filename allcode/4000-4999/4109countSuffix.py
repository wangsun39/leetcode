# 长度为 m - n + 1 的整数数组 ans，其中 ans[k] 表示使排序后的数组等于 target[k..k + n - 1] 的下标 i 的数量。
#
# 数组的 后缀 是从任意下标开始并延伸至数组末尾的子数组。
#
#
#
# 示例 1：
#
# 输入： nums = [2,2,3], target = [2,2,3,2,1,3,2,2]
#
# 输出： [1,1,0,0,0,1]
#
# 解释：
#
# 分别对从下标 0、1 和 2 开始的后缀排序，会依次得到 [3, 2, 2]、[2, 3, 2] 和 [2, 2, 3]。
#
# k = 0：选择 i = 2 可以得到 [2, 2, 3]。
# k = 1：选择 i = 1 可以得到 [2, 3, 2]。
# k = 2, 3, 4：均无法得到对应的子数组。
# k = 5：选择 i = 0 可以得到 [3, 2, 2]。
# 因此，答案为 [1,1,0,0,0,1]。
#
# 示例 2：
#
# 输入： nums = [5,6,5], target = [5,6,5,5,6,5]
#
# 输出： [2,1,0,2]
#
# 解释：
#
# 对从下标 0 开始的后缀排序，会得到 [6, 5, 5]；对从下标 1 或 2 开始的后缀排序，都会得到 [5, 6, 5]。
#
# k = 0：选择 i = 1 或 i = 2 可以得到 [5, 6, 5]。
# k = 1：选择 i = 0 可以得到 [6, 5, 5]。
# k = 2：无法得到 [5, 5, 6]。
# k = 3：选择 i = 1 或 i = 2 可以得到 [5, 6, 5]。
# 因此，答案为 [2, 1, 0, 2]。
#
#
#
# 提示：
#
# n == nums.length
# m == target.length
# 1 <= n <= m <= 105
# 1 <= nums[i], target[i] <= 105

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:

        # z[i] 表示 s 和 s[i:]的最长公共前缀
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            z[0] = n  # 这里根据实际考虑是否为n
            for i in range(1, n):
                if i <= r and z[i - l] < r - i + 1:
                    z[i] = z[i - l]
                else:
                    z[i] = max(0, r - i + 1)
                    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                        z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z

        n, m = len(nums), len(target)
        conn = nums + target

        z = z_function(conn)
        z = z[n:]  # target的每个位置与 nums 的最大公共前缀
        # print(z)
        ans = [0] * (m - n + 1)

        diff = defaultdict(int)  # 滑窗内 nums 与 target 差异的计数
        d = 0  # 滑窗内不同元素计数，统计时只计算nums比target多的元素的计数和
        for i in range(n):
            diff[nums[i]] += 1
            if diff[nums[i]] > 0:
                d += 1
            diff[target[i]] -= 1
            if diff[target[i]] >= 0:
                d -= 1

        l2 = 1  # target 滑窗内最长非递增后缀的长度，且后缀元素和nums后缀相同
        for i in range(n - 2, -1, -1):
            if target[i] >= target[i + 1]:
                l2 += 1
            else:
                break

        for k in range(m - n + 1):
            if d == 0:  # 这步判断很关键
                # 考虑子数组 target[k: k + n] 与 nums 的匹配情况
                right = MIN(z[k], n)  # 相同前缀的最大长度， 只能考虑从 i (<= right) 开始的的后缀排序
                if right == n:  # 完全相同特殊处理
                    right -= 1

                # l2 对应的下标
                left = n - l2
                if right >= left:
                    ans[k] = right - left + 1

            if k < m - n:
                # 考虑 target[i: i + n] 最长非递增后缀的长度
                if target[k + n - 1] >= target[k + n]:
                    l2 = MIN(n, l2 + 1)
                else:
                    l2 = 1

                # 更新diff 和 d
                if diff[target[k]] >= 0:
                    d += 1
                diff[target[k]] += 1

                # print(k, n, k + n)
                if diff[target[k + n]] > 0:
                    d -= 1
                diff[target[k + n]] -= 1

        return ans



so = Solution()
print(so.countSuffix(nums = [8,5,9], target = [6,9,8,5]))  # [0,1]
print(so.countSuffix(nums = [7,6,1], target = [6,1,7]))  # [0]
print(so.countSuffix(nums = [10,4], target = [2,10,4]))  # [0,2]
print(so.countSuffix(nums = [10], target = [3,10]))  # [0,1]
print(so.countSuffix(nums = [5,6,5], target = [5,6,5,5,6,5]))  # [2,1,0,2]
print(so.countSuffix(nums = [2,2,3], target = [2,2,3,2,1,3,2,2]))  # [1,1,0,0,0,1]


