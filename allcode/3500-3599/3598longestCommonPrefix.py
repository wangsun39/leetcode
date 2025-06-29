# 给你一个字符串数组 words，对于范围 [0, words.length - 1] 内的每个下标 i，执行以下步骤：
#
# 从 words 数组中移除下标 i 处的元素。
# 计算修改后的数组中所有 相邻对 之间的 最长公共前缀 的长度。
# 返回一个数组 answer，其中 answer[i] 是移除下标 i 后，相邻对之间最长公共前缀的长度。如果 不存在 相邻对，或者 不存在 公共前缀，则 answer[i] 应为 0。
#
# 字符串的前缀是从字符串的开头开始延伸到任意位置的子字符串。
#
#
#
# 示例 1：
#
# 输入： words = ["jump","run","run","jump","run"]
#
# 输出： [3,0,0,3,3]
#
# 解释：
#
# 移除下标 0：
# words 变为 ["run", "run", "jump", "run"]
# 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3）
# 移除下标 1：
# words 变为 ["jump", "run", "jump", "run"]
# 没有相邻对有公共前缀（长度为 0）
# 移除下标 2：
# words 变为 ["jump", "run", "jump", "run"]
# 没有相邻对有公共前缀（长度为 0）
# 移除下标 3：
# words 变为 ["jump", "run", "run", "run"]
# 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3）
# 移除下标 4：
# words 变为 ["jump", "run", "run", "jump"]
# 最长的相邻对是 ["run", "run"]，其公共前缀为 "run"（长度为 3）
# 示例 2：
#
# 输入： words = ["dog","racer","car"]
#
# 输出： [0,0,0]
#
# 解释：
#
# 移除任意下标都会导致答案为 0。
#
#
# 提示：
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 104
# words[i] 仅由小写英文字母组成。
# words[i] 的长度总和不超过 105。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 2: return [0] * n
        def calc(sa, sb):
            na, nb = len(sa), len(sb)
            res = 0
            for i in range(min(na, nb)):
                if sa[i] != sb[i]: return res
                res += 1
            return res

        c1 = [calc(x, y) for x, y in pairwise(words)]
        c2 = sorted(c1, reverse=True)
        mx3 = c2[:3]
        # counter = Counter(c1)
        ans = [0] * n
        for i in range(n):
            v = []
            if i > 0:
                v.append(c1[i - 1])
            if i < n - 1:
                v.append(c1[i])
            mx3c = mx3[:]
            if 0 < i < n - 1:
                mx3c.append(calc(words[i - 1], words[i + 1]))
            for x in v:
                if x in mx3c:
                    j = mx3c.index(x)
                    if j != -1:
                        mx3c.pop(j)

            if len(mx3c):
                ans[i] = max(mx3c)
        return ans




so = Solution()
print(so.longestCommonPrefix(words = ["f","cfe","feab","fcc","cdfda","fcec","afae","cdeb","dc","bffd","edabe"]))
print(so.longestCommonPrefix(words = ["fec","fef","acaa","adfa","afc","fdbda"]))
print(so.longestCommonPrefix(words = ["dog","racer","car"]))
print(so.longestCommonPrefix(words = ["jump","run","run","jump","run"]))




