# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
#
# 如果不存在这样的子字符串，则返回 0。
#
#
#
# 示例 1：
#
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2：
#
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅由小写英文字母组成
# 1 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)

        def dfs(start, end):
            counter = Counter(s[start: end])
            ids = []
            for i, x in enumerate(s):
                if counter[x] < k:
                    ids.append(i)
            ids.insert(0, -1)
            ids.append(n)
            ans = 0
            for a, b in pairwise(ids):
                if a + 1 == b: continue
                counter = Counter()
                for i in range(a + 1, b):
                    x = s[i]
                    counter[x] += 1
                if all(x >= k for x in counter.values()):
                    ans = max(ans, b - a - 1)
                else:
                    ans = max(ans, dfs(a + 1, b))
            return ans
        return dfs(0, n)



so = Solution()
print(so.longestSubstring(s = "bbaaacbd", k = 3))
print(so.longestSubstring(s = "aaabb", k = 3))

