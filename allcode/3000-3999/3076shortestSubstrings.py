# 给你一个数组 arr ，数组中有 n 个 非空 字符串。
#
# 请你求出一个长度为 n 的字符串 answer ，满足：
#
# answer[i] 是 arr[i] 最短 的子字符串，且它不是 arr 中其他任何字符串的子字符串。如果有多个这样的子字符串存在，answer[i] 应该是它们中字典序最小的一个。如果不存在这样的子字符串，answer[i] 为空字符串。
# 请你返回数组 answer 。
#
#
#
# 示例 1：
#
# 输入：arr = ["cab","ad","bad","c"]
# 输出：["ab","","ba",""]
# 解释：求解过程如下：
# - 对于字符串 "cab" ，最短没有在其他字符串中出现过的子字符串是 "ca" 或者 "ab" ，我们选择字典序更小的子字符串，也就是 "ab" 。
# - 对于字符串 "ad" ，不存在没有在其他字符串中出现过的子字符串。
# - 对于字符串 "bad" ，最短没有在其他字符串中出现过的子字符串是 "ba" 。
# - 对于字符串 "c" ，不存在没有在其他字符串中出现过的子字符串。
# 示例 2：
#
# 输入：arr = ["abc","bcd","abcd"]
# 输出：["","","abcd"]
# 解释：求解过程如下：
# - 对于字符串 "abc" ，不存在没有在其他字符串中出现过的子字符串。
# - 对于字符串 "bcd" ，不存在没有在其他字符串中出现过的子字符串。
# - 对于字符串 "abcd" ，最短没有在其他字符串中出现过的子字符串是 "abcd" 。
#
#
# 提示：
#
# n == arr.length
# 2 <= n <= 100
# 1 <= arr[i].length <= 20
# arr[i] 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        counter = Counter()
        sl = []
        for s in arr:
            ss = set()
            m = len(s)
            for i in range(m):
                for j in range(i, m):
                    ss.add(s[i: j + 1])
            sl.append(ss)
            for sub in ss:
                counter[sub] += 1
        n = len(arr)
        ans = [''] * n
        for i, x in enumerate(arr):
            for y in sl[i]:
                if counter[y] == 1 and (ans[i] == '' or len(ans[i]) > len(y) or (len(ans[i]) == len(y) and ans[i] > y)):
                    ans[i] = y
        return ans


so = Solution()
print(so.shortestSubstrings(arr = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]))
print(so.shortestSubstrings(arr = ["cab","ad","bad","c"]))
print(so.shortestSubstrings(arr = ["abc","bcd","abcd"]))




