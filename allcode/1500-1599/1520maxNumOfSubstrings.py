# 给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：
#
# 这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[x..y] ，要么 j < x 要么 i > y 。
# 如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。
# 请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。
#
# 请注意，你可以以 任意 顺序返回最优解的子字符串。
#
#
#
# 示例 1：
#
# 输入：s = "adefaddaccc"
# 输出：["e","f","ccc"]
# 解释：下面为所有满足第二个条件的子字符串：
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# 如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择 "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。
# 示例 2：
#
# 输入：s = "abbaccd"
# 输出：["d","bb","cc"]
# 解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
#
#
# 提示：
#
# 1 <= s.length <= 10^5
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        i2c = {i: c for i, c in enumerate(ascii_lowercase)}
        d1 = defaultdict(list)  # d1[c2i[x]]  记录x的最小下标和最大下标
        for i, x in enumerate(s):
            if c2i[x] in d1:
                d1[c2i[x]][1] = i
            else:
                d1[c2i[x]] = [i, i]
        d2 = defaultdict(set)  # d2[c2i[x]]  记录x的范围内包含的其他字符
        for j, [l, r] in d1.items():
            for i in range(l, r + 1):
                if s[i] != i2c[j]:
                    d2[j].add(c2i[s[i]])

        fa = list(range(26))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(26):
            for j in range(i + 1, 26):
                # 仅当a中有b，b中有a时，a和b的区间可以合并成一个组
                if j in d2[i] and i in d2[j]:
                    union(i, j)

        for i in range(26):
            find(i)
        group = defaultdict(list)  # 在一个子区间内的所有字符
        for i in range(26):
            if i not in d1: continue
            group[fa[i]].append(i)
        seg = []  # 每个组的区间范围
        for grp in group.values():
            seg.append([min(d1[x][0] for x in grp), max(d1[x][1] for x in grp)])

        m = len(seg)
        valid = set(range(m))  # 最终的区间
        for i in range(m):
            for j in range(m):
                if i == j: continue
                # 一个组包含另一个组，那么外层的组不能成为最终区间
                if seg[i][0] <= seg[j][0] and seg[i][1] >= seg[j][1]:
                    valid.remove(i)
                    break
        ans = []
        for i in valid:
            l, r = seg[i]
            ans.append(s[l: r + 1])
        return ans




so = Solution()
print(so.maxNumOfSubstrings(s = "zyz"))
print(so.maxNumOfSubstrings(s = "adefaddaccc"))
print(so.maxNumOfSubstrings(s = "abbaccd"))




