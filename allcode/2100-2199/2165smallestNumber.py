# 给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。
#
# 返回不含前导零且值最小的重排数字。
#
# 注意，重排各位数字后，num 的符号不会改变。
#
#
#
# 示例 1：
#
# 输入：num = 310
# 输出：103
# 解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。
# 不含任何前导零且值最小的重排数字是 103 。
# 示例 2：
#
# 输入：num = -7605
# 输出：-7650
# 解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
# 不含任何前导零且值最小的重排数字是 -7650 。
#
#
# 提示：
#
# -1015 <= num <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestNumber(self, num: int) -> int:

        if num <= 0:
            s = list(str(-num))
            s.sort(reverse=True)
            return -int(''.join(s))
        s = list(str(num))
        s.sort()
        i = 0
        while True:
            if s[i] != '0': break
            i += 1
        s = [s[i]] + s[:i] + s[i + 1:]
        return int(''.join(s))


so = Solution()
print(so.smallestNumber(num = 310))
print(so.smallestNumber(num = -7605))




