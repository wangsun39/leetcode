# 给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：
#
# 选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。
# 比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。
#
# 如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。
#
# 一个 子字符串 定义为一个字符串中连续的若干字符。
#
#
#
# 示例 1：
#
# 输入：s = "84532", t = "34852"
# 输出：true
# 解释：你可以按以下操作将 s 转变为 t ：
# "84532" （从下标 2 到下标 3）-> "84352"
# "84352" （从下标 0 到下标 2） -> "34852"
# 示例 2：
#
# 输入：s = "34521", t = "23415"
# 输出：true
# 解释：你可以按以下操作将 s 转变为 t ：
# "34521" -> "23451"
# "23451" -> "23415"
# 示例 3：
#
# 输入：s = "12345", t = "12435"
# 输出：false
# 示例 4：
#
# 输入：s = "1", t = "2"
# 输出：false
#
#
# 提示：
#
# s.length == t.length
# 1 <= s.length <= 105
# s 和 t 都只包含数字字符，即 '0' 到 '9' 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, x in enumerate(s):
            pos[x].append(i)
        for x in t:
            # 当前x要从后面的位置移动到这个位置，需要保证在它前面的数字都比它大，否则就失败了
            if len(pos[x]) == 0: return False
            px = pos[x][0]
            for u in pos.keys():
                if len(pos[u]) and u < x and pos[u][0] < px:
                    return False
            pos[x].pop(0)
        return True


so = Solution()
print(so.isTransformable(s = "1", t = "2"))
print(so.isTransformable(s = "84532", t = "34852"))




