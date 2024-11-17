# 给你一个 二进制 字符串 s 和一个整数 k。
#
# 另给你一个二维整数数组 queries ，其中 queries[i] = [li, ri] 。
#
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
#
# 字符串中 0 的数量最多为 k。
# 字符串中 1 的数量最多为 k。
# 返回一个整数数组 answer ，其中 answer[i] 表示 s[li..ri] 中满足 k 约束 的
# 子字符串
#  的数量。
#
#
#
# 示例 1：
#
# 输入：s = "0001111", k = 2, queries = [[0,6]]
#
# 输出：[26]
#
# 解释：
#
# 对于查询 [0, 6]， s[0..6] = "0001111" 的所有子字符串中，除 s[0..5] = "000111" 和 s[0..6] = "0001111" 外，其余子字符串都满足 k 约束。
#
# 示例 2：
#
# 输入：s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]
#
# 输出：[15,9,3]
#
# 解释：
#
# s 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。
#
#
#
# 提示：
#
# 1 <= s.length <= 105
# s[i] 是 '0' 或 '1'
# 1 <= k <= s.length
# 1 <= queries.length <= 105
# queries[i] == [li, ri]
# 0 <= li <= ri < s.length
# 所有查询互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        right = [0] * n  # s[i]开始的子串，最大的右端点right[i]能保证子串是满足k约束的
        l = 0
        c0 = c1 = 0
        for r in range(n):
            if s[r] == '0': c0 += 1
            else: c1 += 1
            if c0 <= k or c1 <= k:
                continue
            while l <= r:
                if s[l] == '0': c0 -= 1
                else: c1 -= 1
                right[l] = r - 1
                l += 1
                if c0 <= k or c1 <= k:
                    break
        while l < n:
            right[l] = n - 1
            l += 1
        # 其实每个以 right[i] 结尾的子串，满足k约束左侧的最小值就是i
        # 因此计算出left数组
        left = [-1] * n
        for i, x in enumerate(right):
            if left[x] == -1:
                left[x] = i
        for i in range(n - 2, -1, -1):
            if left[i] == -1:
                left[i] = left[i + 1]
        # 将left数组转换为，以i结尾的子串，满足k约束的最大长度
        left = [i - x + 1 for i, x in enumerate(left)]
        # print(left)
        # print(right)
        s = list(accumulate(left, initial=0))
        ans = []
        for x, y in queries:
            if right[x] >= y:
                # 所有子数组都满足条件，等差数列求和
                ans.append((y - x + 2) * (y - x + 1) // 2)
            else:
                # [x, right[x]]的子数组都是满足条件的，[right[x] + 1, y] 就是按left的数组的区间和
                ans.append((right[x] - x + 2) * (right[x] - x + 1) // 2 + s[y + 1] - s[right[x] + 1])
        return ans



so = Solution()
print(so.countKConstraintSubstrings(s = "0001111", k = 2, queries = [[0,6]]))




