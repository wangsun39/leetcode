# 给定一个数字字符串 num，比如 "123456579"，我们可以将它分成「斐波那契式」的序列 [123, 456, 579]。
#
# 形式上，斐波那契式 序列是一个非负整数列表 f，且满足：
#
# 0 <= f[i] < 231 ，（也就是说，每个整数都符合 32 位 有符号整数类型）
# f.length >= 3
# 对于所有的0 <= i < f.length - 2，都有 f[i] + f[i + 1] = f[i + 2]
# 另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
#
# 返回从 num 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。
#
#
#
# 示例 1：
#
# 输入：num = "1101111"
# 输出：[11,0,11,11]
# 解释：输出 [110,1,111] 也可以。
# 示例 2：
#
# 输入: num = "112358130"
# 输出: []
# 解释: 无法拆分。
# 示例 3：
#
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
#
#
# 提示：
#
# 1 <= num.length <= 200
# num 中只含有数字

from leetcode.allcode.competition.mypackage import *

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        if all(x == '0' for x in num):
            return [0] * n

        @cache
        def dfs(i, j, k):
            # [i, j] [j+1,k] 分别是最后两段的情况下，返回后面的分组
            if k == n - 1: return []
            if num[k + 1] == '0': return None
            # print(i, j, k)
            v1, v2 = int(num[i: j + 1]), int(num[j + 1: k + 1])
            v3 = v1 + v2
            if v3 >= 2 ** 31: return None
            s3 = str(v3)
            if num[k + 1:].startswith(s3):
                res = dfs(j + 1, k, k + len(s3))
                if res is None:
                    return None
                return [v3] + res
            return None
        hi = 1 if num[0] == '0' else n - 2
        for j in range(hi):
            hj = j + 2 if num[j + 1] == '0' else n - 1
            for k in range(j + 1, hj):
                ans = dfs(0, j, k)
                if ans is None: continue
                ans = [int(num[:j + 1]), int(num[j + 1: k + 1])] + ans
                return ans
        return []


so = Solution()
print(so.splitIntoFibonacci(num = "1101111"))

