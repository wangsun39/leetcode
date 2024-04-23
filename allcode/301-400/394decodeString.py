# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
# 提示：
#
# 1 <= s.length <= 30
# s 由小写英文字母、数字和方括号 '[]' 组成
# s 保证是一个 有效 的输入。
# s 中所有整数的取值范围为 [1, 300]

from leetcode.allcode.competition.mypackage import *

class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def dfs(start):
            # 最外层调用就是从0开始处理到最后，遇到[开始递归
            # 对于内层递归来说：start是 "[" 位置，返回配对的 "]" 位置
            i = start
            res = []
            while i < n:
                if s[i].isalpha():
                    res.append(s[i])
                elif s[i].isdigit():
                    n_i = i
                    while s[i + 1] != '[':
                        i += 1
                    multiple = int(s[n_i: i + 1])
                    i, l = dfs(i + 1)  # 递归内部的括号
                    res += l * multiple
                    # i += 1
                elif s[i] == '[':
                    pass
                else:  # ']'
                    break
                i += 1
            return i, res

        _, ans = dfs(0)
        return ''.join(ans)

so = Solution()
print(so.decodeString("3[a]"))
print(so.decodeString("3[a]2[bc]"))
print(so.decodeString("3[a2[c]]"))
print(so.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
print(so.decodeString("abc3[cd]xyz"))  # "abccdcdcdxyz"

