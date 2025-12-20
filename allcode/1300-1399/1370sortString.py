# 给你一个字符串 s ，请你根据下面的算法重新构造字符串：
#
# 从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出比上一个添加字符更大的 最小 字符，将它 接在 结果字符串后面。
# 重复步骤 2 ，直到你没法从 s 中选择字符。
# 从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
# 从 s 剩余字符中选出比上一个添加字符更小的 最大 字符，将它 接在 结果字符串后面。
# 重复步骤 5 ，直到你没法从 s 中选择字符。
# 重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
# 在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。
#
# 请你返回将 s 中字符重新排序后的 结果字符串 。
#
#
#
# 示例 1：
#
# 输入：s = "aaaabbbbcccc"
# 输出："abccbaabccba"
# 解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
# 第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
# 第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
# 第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
# 第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
# 示例 2：
#
# 输入：s = "rat"
# 输出："art"
# 解释：单词 "rat" 在上述算法重排序以后变成 "art"
#
#
# 提示：
#
# 1 <= s.length <= 500
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        arr = []
        for x in ascii_lowercase:
            if counter[x]:
                arr.append([x, counter[x]])
        ans = []
        m = len(arr)
        while len(ans) < n:
            for i in range(m):
                x, c = arr[i]
                if c:
                    ans.append(x)
                    arr[i][1] -= 1
            for i in range(m - 1, -1, -1):
                x, c = arr[i]
                if c:
                    ans.append(x)
                    arr[i][1] -= 1
        return ''.join(ans)


so = Solution()
print(so.sortString("aaaabbbbcccc"))




