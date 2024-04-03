# 给你一个字符串 s 。
#
# 请你进行以下操作直到 s 为 空 ：
#
# 每次操作 依次 遍历 'a' 到 'z'，如果当前字符出现在 s 中，那么删除出现位置 最早 的该字符。
# 请你返回进行 最后 一次操作 之前 的字符串 s 。
#
#
#
# 示例 1：
#
# 输入：s = "aabcbbca"
# 输出："ba"
# 解释：我们进行以下操作：
# - 删除 s = "aabcbbca" 中加粗加斜字符，得到字符串 s = "abbca" 。
# - 删除 s = "abbca" 中加粗加斜字符，得到字符串 s = "ba" 。
# - 删除 s = "ba" 中加粗加斜字符，得到字符串 s = "" 。
# 进行最后一次操作之前的字符串为 "ba" 。
# 示例 2：
#
# 输入：s = "abcd"
# 输出："abcd"
# 解释：我们进行以下操作：
# - 删除 s = "abcd" 中加粗加斜字符，得到字符串 s = "" 。
# 进行最后一次操作之前的字符串为 "abcd" 。
#
#
# 提示：
#
# 1 <= s.length <= 5 * 105
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        pos = {}
        for i, x in enumerate(s):
            pos[x] = i
        counter = Counter(s)
        mx = max(counter.values())
        s = set(x for x, v in counter.items() if v == mx)
        pos = sorted([[v, k] for k, v in pos.items() if k in s])
        ans = [k for _, k in pos]
        return ''.join(ans)


so = Solution()
print(so.lastNonEmptyString("aabcbbca"))
print(so.lastNonEmptyString("abcd"))




