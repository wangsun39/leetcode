# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
#
# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
#
# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
#
#
#
# 示例 1：
#
# 输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
# 示例 2：
#
# 输入：a = 2, b = 2, c = 1
# 输出："aabbc"
# 示例 3：
#
# 输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。
#
#
# 提示：
#
# 0 <= a, b, c <= 100
# a + b + c > 0


from typing import List

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l1 = [a, b, c]
        l1.sort()
        l2 = []
        for e in l1:
            if e == a and 'a' not in l2:
                l2.append('a')
            elif e == b and 'b' not in l2:
                l2.append('b')
            else:
                l2.append('c')
        print(l1)
        print(l2)
        x, y, z = l1[0], l1[1], l1[2]
        if z >= (x + y) * 2 + 2:
            z = (x + y) * 2 + 2
            res = (l2[2] * 2 + l2[1]) * y + (l2[2] * 2 + l2[0]) * x + l2[2] * 2
            # return ''
        elif (x + y) + 1 <= z <= (x + y) * 2 + 2:
            remain = z % (x + y + 1)
            if remain < x:
                res = (l2[2] * 2 + l2[0]) * remain
                res += (l2[2] + l2[0]) * (x - remain) + (l2[2] + l2[1]) * y + l2[2]
            else:
                res = (l2[2] * 2 + l2[0]) * x
                res += (l2[2] * 2 + l2[1]) * (remain - x) + (l2[2] + l2[1]) * (y - remain + x) + l2[2]
        elif y == z:
            res = (l2[2] + l2[1] + l2[0]) * x + (l2[2] + l2[1]) * (z - x)
        else:
            w = y + x - z + 1
            res = (l2[2] + l2[1] + l2[0]) * w
            res += (l2[2] + l2[1]) * (y - w) + (l2[2] + l2[0]) * (x - w) + l2[2]

        return res

so = Solution()
print(so.longestDiverseString(1, 4, 5))
print(so.longestDiverseString(2, 2, 1))
print(so.longestDiverseString(7, 1, 0))
print(so.longestDiverseString(1, 1, 7))
print(so.longestDiverseString(5, 2, 1))




