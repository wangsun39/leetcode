# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#
# 示例 1：
#
#  输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
#  输出：-1
#  说明：不存在返回-1。
# 示例 2：
#
#  输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
#  输出：4
# 提示:
#
# words的长度在[1, 1000000]之间

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findString(self, words: List[str], s: str) -> int:
        n = len(words)
        ans = -1

        def dfs(l, r):
            # 返回-1: 区间内都小于s
            # 返回 1: 区间内都大于s
            # 返回 0: 区间内存在等于s
            # 返回 2: 不存在s
            # 返回-2: 区间内都是空串
            nonlocal ans
            if l == r:
                if words[l] == '': return None
                if words[l] == s:
                    ans = l
                    return 0
                if words[l] < s:
                    return -1
                return 1
            mid = (l + r) // 2
            r1 = dfs(l, mid)
            if r1 in (1, 2, 0): return r1
            r2 = dfs(mid + 1, r)
            if r2 in (2, 0, -1): return r2
            if r1 == -1:
                if r2 == 1:
                    return 2
                return -1
            else:  # -2
                return r2  # 1 or -2

        dfs(0, n - 1)
        return ans







so = Solution()
print(so.findString(["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"))




