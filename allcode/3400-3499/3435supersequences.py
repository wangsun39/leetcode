# 给你一个字符串数组 words 。请你找到 words 所有 最短公共超序列 ，且确保它们互相之间无法通过排列得到。
#
# 最短公共超序列 指的是一个字符串，words 中所有字符串都是它的子序列，且它的长度 最短 。
#
# 请你返回一个二维整数数组 freqs ，表示所有的最短公共超序列，其中 freqs[i] 是一个长度为 26 的数组，它依次表示一个最短公共超序列的所有小写英文字母的出现频率。你可以以任意顺序返回这个频率数组。
#
# 排列 指的是一个字符串中所有字母重新安排顺序以后得到的字符串。
#
# 一个 子序列 是从一个字符串中删除一些（也可以不删除）字符后，剩余字符不改变顺序连接得到的 非空 字符串。
#
#
#
# 示例 1：
#
# 输入：words = ["ab","ba"]
#
# 输出：[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#
# 解释：
#
# 两个最短公共超序列分别是 "aba" 和 "bab" 。输出分别是两者的字母出现频率。
#
# 示例 2：
#
# 输入：words = ["aa","ac"]
#
# 输出：[[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#
# 解释：
#
# 两个最短公共超序列分别是 "aac" 和 "aca" 。由于它们互为排列，所以只保留 "aac" 。
#
# 示例 3：
#
# 输入：words = ["aa","bb","cc"]
#
# 输出：[[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#
# 解释：
#
# "aabbcc" 和它所有的排列都是最短公共超序列。
#
#
#
# 提示：
#
# 1 <= words.length <= 256
# words[i].length == 2
# words 中所有字符串由不超过 16 个互不相同的小写英文字母组成。
# words 中的字符串互不相同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        s = set()
        for x, y in words:
            s.add(x)
            s.add(y)
        ch = list(s)
        m = len(ch)
        ans = []

        def check(one):
            # 检查one中的字符是否不能构成一个环
            if len(one) == 0: return True
            g = defaultdict(set)
            pre_num = defaultdict(int)
            for x, y in words:  # x 先于 y , 原图需要反转时，可以写成 for y, x in conditions:
                if x in one and y in one:
                    if y not in g[x]:
                        g[x].add(y)
                        pre_num[y] += 1
            queue = deque([i for i in one if pre_num[i] == 0])  # deque 在操作大数组时，性能比 list 好很多
            ans = []
            while len(queue):
                q = queue.popleft()
                ans.append(q)
                for x in g[q]:
                    pre_num[x] -= 1
                    if pre_num[x] == 0:
                        queue.append(x)
            if len(ans) != len(one):
                return False  # 存在圈
            return True

        mn = inf  # 最短超序列中元素个数
        for mask in range(1 << m):
            # 枚举最终出现两次的字符
            one = set()  # 仅出现一次的字符
            for i in range(m):
                if (mask & (1 << i)) == 0:
                    one.add(ch[i])
            x = len(one) + (m - len(one)) * 2  # 此超序列中元素个数
            if x <= mn and check(one):
                l = [0] * 26
                for i in range(m):
                    if (mask & (1 << i)) == 0:
                        l[c2i[ch[i]]] = 1
                    else:
                        l[c2i[ch[i]]] = 2
                ans.append(l)
                mn = x
        if mn == inf: return []
        ans = [x for x in ans if sum(x) == mn]

        return ans



so = Solution()
print(so.supersequences(words = ["ab","ba"]))




