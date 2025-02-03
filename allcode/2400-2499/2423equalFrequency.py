# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
#
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
#
# 注意：
#
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。
#
#
# 示例 1：
#
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。
# 示例 2：
#
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
#
#
# 提示：
#
# 2 <= word.length <= 100
# word 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def equalFrequency(self, word: str) -> bool:
        ct = Counter(word)
        ct2 = Counter(ct.values())
        if len(ct2) > 2: return False
        if len(ct2) == 1: return 1 in ct2.keys() or 1 in ct2.values()
        if ct2[1] == 1: return True
        k = sorted(list(ct2.keys()))
        return k[1] - k[0] == 1 and ( ct2[k[1]] == 1)

    def equalFrequency1(self, word: str) -> bool:
        # 2023/7/8
        counter = Counter(word)
        cc = sorted(list(counter.values()))
        cc[-1] -= 1  # 删除第一个
        if all(x == cc[0] for x in cc):
            return True
        cc[-1] += 1
        if cc[0] == 1 and all(x == cc[1] for x in cc[1:]):  # 删除最后一个
            return True

        return False






so = Solution()
print(so.equalFrequency(word = "acbda"))  # True
print(so.equalFrequency(word = "cbccca"))  # False
print(so.equalFrequency(word = "cccd"))  # True
print(so.equalFrequency(word = "abcc"))  # True
print(so.equalFrequency(word = "zz"))  # True
print(so.equalFrequency(word = "ddaccb"))  # False
print(so.equalFrequency(word = "bac"))  # True
print(so.equalFrequency(word = "aazz"))  # False




