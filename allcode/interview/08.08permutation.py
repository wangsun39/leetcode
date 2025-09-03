# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
#
# 示例 1：
#
#  输入：S = "qqe"
#  输出：["eqq","qeq","qqe"]
# 示例 2：
#
#  输入：S = "ab"
#  输出：["ab", "ba"]
# 提示:
#
# 字符都是英文字母。
# 字符串长度在[1, 9]之间。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def permutation(self, S: str) -> List[str]:
        counter = Counter(S)
        ans = []

        @cache
        def dfs(pre):
            res = []
            if all(x == 0 for x in counter.values()):
                ans.append(pre)
                return
            for k, v in counter.items():
                if v == 0: continue
                counter[k] -= 1
                dfs(pre + k)
                counter[k] += 1
            return res

        dfs('')
        return ans

so = Solution()
print(so.permutation("qqe"))




