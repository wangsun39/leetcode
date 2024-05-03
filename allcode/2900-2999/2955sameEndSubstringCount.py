# 给定一个 下标从0开始 的字符串 s，以及一个二维整数数组 queries，其中 queries[i] = [li, ri] 表示 s 中从索引 li 开始到索引 ri 结束的子串（包括两端），即 s[li..ri]。
#
# 返回一个数组 ans，其中 ans[i] 是 queries[i] 的 同端 子串的数量。
#
# 如果一个 下标从0开始 且长度为 n 的字符串 t 两端的字符相同，即 t[0] == t[n - 1]，则该字符串被称为 同端。
#
# 子串 是一个字符串中连续的非空字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
# 输出：[1,5,5,10]
# 解释：每个查询的同端子串如下：
# 第一个查询：s[0..0] 是 "a"，有 1 个同端子串："a"。
# 第二个查询：s[1..4] 是 "bcaa"，有 5 个同端子串："bcaa", "bcaa", "bcaa", "bcaa", "bcaa"。
# 第三个查询：s[2..5] 是 "caab"，有 5 个同端子串："caab", "caab", "caab", "caab", "caab"。
# 第四个查询：s[0..5] 是 "abcaab"，有 10 个同端子串："abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab"。
# 示例 2：
#
# 输入：s = "abcd", queries = [[0,3]]
# 输出：[4]
# 解释：唯一的查询是 s[0..3]，它有 4 个同端子串："abcd", "abcd", "abcd", "abcd"。
#
#
# 提示：
#
# 2 <= s.length <= 3 * 104
# s 仅包含小写英文字母。
# 1 <= queries.length <= 3 * 104
# queries[i] = [li, ri]
# 0 <= li <= ri < s.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        counter = [[0] * 26]
        for i in range(1, n + 1):
            counter.append(counter[-1][:])
            counter[-1][c2i[s[i - 1]]] += 1
        ans = []
        for a, b in queries:
            cnt = 0
            for i in range(26):
                v = counter[b + 1][i] - counter[a][i]
                if v >= 1:
                    cnt += v * (v - 1) // 2 + v
            ans.append(cnt)
        return ans

so = Solution()
print(so.sameEndSubstringCount(s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]))
print(so.sameEndSubstringCount(s = "abcd", queries = [[0,3]]))




