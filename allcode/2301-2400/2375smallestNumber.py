# 给你下标从 0 开始、长度为 n的字符串pattern，它包含两种字符，'I'表示 上升，'D'表示 下降。
#
# 你需要构造一个下标从 0开始长度为n + 1的字符串，且它要满足以下条件：
#
# num包含数字'1'到'9'，其中每个数字至多使用一次。
# 如果pattern[i] == 'I'，那么num[i] < num[i + 1]。
# 如果pattern[i] == 'D'，那么num[i] > num[i + 1]。
# 请你返回满足上述条件字典序 最小的字符串num。
#
#
#
# 示例 1：
#
# 输入：pattern = "IIIDIDDD"
# 输出："123549876"
# 解释：
# 下标 0 ，1 ，2 和 4 处，我们需要使 num[i] < num[i+1] 。
# 下标 3 ，5 ，6 和 7 处，我们需要使 num[i] > num[i+1] 。
# 一些可能的 num 的值为 "245639871" ，"135749862" 和 "123849765" 。
# "123549876" 是满足条件最小的数字。
# 注意，"123414321" 不是可行解因为数字 '1' 使用次数超过 1 次。
# 示例 2：
#
# 输入：pattern = "DDD"
# 输出："4321"
# 解释：
# 一些可能的 num 的值为 "9876" ，"7321" 和 "8742" 。
# "4321" 是满足条件最小的数字。
#
#
# 提示：
#
# 1 <= pattern.length <= 8
# pattern只包含字符'I' 和'D' 。


from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def helper(pattern):
            if pattern == 'I':
                return '12'
            if pattern == 'D':
                return '21'
            n = len(pattern)
            pos = pattern.rfind('I')
            ans = ''
            if pos == -1:
                for i in range(n + 1, 0, -1):
                    ans += str(i)
                return ans
            sub2 = ''
            i = n + 1
            count = 0
            # for i in range(n + 1, n - pos + 1, -1):
            while count < n - pos:
                sub2 += str(i)
                count += 1
                i -= 1
            sub1 = helper(pattern[:pos])
            return sub1 + sub2
        return helper(pattern)



so = Solution()
print(so.smallestNumber("IIIDDD"))
print(so.smallestNumber("IIIDIDDD"))
print(so.smallestNumber("DDD"))




