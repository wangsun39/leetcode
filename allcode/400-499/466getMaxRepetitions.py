# 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。
#
# 例如，str == ["abc", 3] =="abcabcabc" 。
# 如果可以从 s2中删除某些字符使其变为 s1，则称字符串 s1可以从字符串 s2 获得。
#
# 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
# 现在给你两个字符串 s1和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。
#
# 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1获得。
#
#
#
# 示例 1：
#
# 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# 输出：2
# 示例 2：
#
# 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# 输出：1
#
#
# 提示：
#
# 1 <= s1.length, s2.length <= 100
# s1 和 s2 由小写英文字母组成
# 1 <= n1, n2 <= 106



class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        def calc(s1, n1, s2):
            # 不断分别重复s1和s2，在s1的序列中不断重复查找s2的给个字符，并在每次查找到最后一个s2的字符时，记录
            # s1中所对应的字符在s1中的下标，直至发现有重复下标时结束
            N1, N2 = len(s1), len(s2)
            i, j = 0, 0
            num1, num2 = 0, 0  # 记录s1，s2分别循环多少次
            first = []  # s1与第一个s2匹配完的位置，[匹配结束时num1, 匹配结束时s2的结尾在s1中的下标]
            while True:
                if num1 >= n1:
                    return None, num2, None
                pos = s1.find(s2[j], i)
                if pos == -1:
                    i = 0
                    num1 += 1
                    continue
                i = pos + 1
                j += 1
                if j == N2:
                    if len(first) > 0 and pos == first[1]:
                        complete = True if num1 - first[0] == (num2 + 1) * (first[0] + 1) else False
                        return num1 - first[0], num2, complete
                    if len(first) == 0:
                        first = [num1, pos]
                    num2 += 1
                    j = 0
                if i == N1:
                    i = 0
                    num1 += 1

        num1, num2, complete = calc(s1, n1, s2)
        if num1 is None:
            # str1中还未出现对s2的循环覆盖周期
            return num2 // n2
        if complete:
            # num1个s1刚好覆盖num2个s2
            numOfCycleS2InStr1 = n1 // num1  # str1中会出现多少次对s2的完整的循环覆盖
            remainOfS1 = n1 % num1  # str1中会出现剩余的s1数量
            numOfS2InStr1 = numOfCycleS2InStr1 * num2  # pre_num1个s1中会出现多少次s2
        else:
            numOfCycleS2InStr1 = (n1 - 1) // num1
            remainOfS1 = (n1 - 1) % num1 + 1
            numOfS2InStr1 = numOfCycleS2InStr1 * num2
        _, numOfRemainOfS2, _ = calc(s1, remainOfS1, s2)
        numOfS2InStr1 += numOfRemainOfS2
        return numOfS2InStr1 // n2


so = Solution()
print(so.getMaxRepetitions(s1 = "bacaba", n1 = 3, s2 = "abacab", n2 = 1))  # 2
print(so.getMaxRepetitions(s1 = "bacababacaba", n1 = 2, s2 = "abacab", n2 = 1))  # 3
print(so.getMaxRepetitions(s1 = "bacba", n1 = 4, s2 = "ab", n2 = 2))  # 3
print(so.getMaxRepetitions(s1 = "baba", n1 = 11, s2 = "baab", n2 = 1))  # 7
print(so.getMaxRepetitions(s1 = "abba", n1 = 1, s2 = "ab", n2 = 1))  # 1


print(so.getMaxRepetitions(s1 = "ab", n1 = 8, s2 = "abab", n2 = 2))  # 2
print(so.getMaxRepetitions(s1 = "ab", n1 = 4, s2 = "aba", n2 = 2))  # 1
print(so.getMaxRepetitions(s1 = "acb", n1 = 4, s2 = "bca", n2 = 2))
print(so.getMaxRepetitions(s1 = "acb", n1 = 4, s2 = "abc", n2 = 2))  # 1
print(so.getMaxRepetitions(s1 = "bacba", n1 = 4, s2 = "ab", n2 = 2))  # 3
print(so.getMaxRepetitions(s1 = "acb", n1 = 4, s2 = "ab", n2 = 2))  # 2
print(so.getMaxRepetitions(s1 = "aaa", n1 = 3, s2 = "aa", n2 = 1))  # 4

