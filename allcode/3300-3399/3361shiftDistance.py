# 给你两个长度相同的字符串 s 和 t ，以及两个整数数组 nextCost 和 previousCost 。
#
# 一次操作中，你可以选择 s 中的一个下标 i ，执行以下操作 之一 ：
#
# 将 s[i] 切换为字母表中的下一个字母，如果 s[i] == 'z' ，切换后得到 'a' 。操作的代价为 nextCost[j] ，其中 j 表示 s[i] 在字母表中的下标。
# 将 s[i] 切换为字母表中的上一个字母，如果 s[i] == 'a' ，切换后得到 'z' 。操作的代价为 previousCost[j] ，其中 j 是 s[i] 在字母表中的下标。
# 切换距离 指的是将字符串 s 变为字符串 t 的 最少 操作代价总和。
#
# 请你返回从 s 到 t 的 切换距离 。
#
#
#
# 示例 1：
#
# 输入：s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
# 输出：2
#
# 解释：
#
# 选择下标 i = 0 并将 s[0] 向前切换 25 次，总代价为 1 。
# 选择下标 i = 1 并将 s[1] 向后切换 25 次，总代价为 0 。
# 选择下标 i = 2 并将 s[2] 向前切换 25 次，总代价为 1 。
# 选择下标 i = 3 并将 s[3] 向后切换 25 次，总代价为 0 。
# 示例 2：
#
# 输入：s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#
# 输出：31
#
# 解释：
#
# 选择下标 i = 0 并将 s[0] 向前切换 9 次，总代价为 9 。
# 选择下标 i = 1 并将 s[1] 向后切换 10 次，总代价为 10 。
# 选择下标 i = 2 并将 s[2] 向前切换 1 次，总代价为 1 。
# 选择下标 i = 3 并将 s[3] 向后切换 11 次，总代价为 11 。
#
#
# 提示：
#
# 1 <= s.length == t.length <= 105
# s 和 t 都只包含小写英文字母。
# nextCost.length == previousCost.length == 26
# 0 <= nextCost[i], previousCost[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        ssp = sum(previousCost)
        nextCost += nextCost
        # previousCost += previousCost
        sn = list(accumulate(nextCost, initial=0))
        sp = list(accumulate(previousCost, initial=0))

        ans = 0
        n = len(s)
        for i in range(n):
            if t[i] > s[i]:   # nextCost 数组的中间的区间 [c2i[s[i]], c2i[t[i]])   previousCost 数组刨除中间的区间  (c2i[s[i]], c2i[t[i]]]
                ans += min(sn[c2i[t[i]]] - sn[c2i[s[i]]], ssp - (sp[c2i[t[i]] + 1] - sp[c2i[s[i]] + 1]))
            elif t[i] < s[i]:   # nextCost 数组的中间的区间 [c2i[s[i]], c2i[t[i]] + 26)   previousCost 数组中间的区间  (c2i[t[i]], c2i[s[i]])
                ans += min(sp[c2i[s[i]] + 1] - sp[c2i[t[i]] + 1], sn[c2i[t[i]] + 26] - sn[c2i[s[i]]])
        return ans



so = Solution()
print(so.shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))




