# 给你一个非空的字符串 s 和一个整数 k ，你要将这个字符串 s 中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离 至少 为 k 。如果无法做到，请返回一个空字符串 ""。
#
#
#
# 示例 1：
#
# 输入: s = "aabbcc", k = 3
# 输出: "abcabc"
# 解释: 相同的字母在新的字符串中间隔至少 3 个单位距离。
# 示例 2:
#
# 输入: s = "aaabc", k = 3
# 输出: ""
# 解释: 没有办法找到可能的重排结果。
# 示例 3:
#
# 输入: s = "aaadbbcc", k = 2
# 输出: "abacabcd"
# 解释: 相同的字母在新的字符串中间隔至少 2 个单位距离。
#
#
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 仅由小写英文字母组成
# 0 <= k <= s.length


from leetcode.allcode.competition.mypackage import *

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counter = Counter(s)
        hp = []  # 存放计数的大顶堆
        for kk, v in counter.items():
            heappush(hp, [-v, kk])
        ans = []
        while hp:
            if len(hp) < k and hp[0][0] != -1:
                return ''
            cnt = []  #
            for i in range(min(k, len(hp))):  # 一次取出 k 个计数最多的元素
                c, x = heappop(hp)
                ans.append(x)
                if c < -1:
                    cnt.append([c + 1, x])
            for pair in cnt:
                heappush(hp, pair)
        return ''.join(ans)

so = Solution()
print(so.rearrangeString(s = "bab", k = 2))
print(so.rearrangeString(s = "a", k = 0))
print(so.rearrangeString(s = "aabbcc", k = 3))



