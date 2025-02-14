# 给你一个混合字符串s，请你返回 s中 第二大 的数字，如果不存在第二大的数字，请你返回 -1。
#
# 混合字符串 由小写英文字母和数字组成。
#
# 
#
# 示例 1：
#
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
# 示例 2：
#
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
# 
#
# 提示：
#
# 1 <= s.length <= 500
# s只包含小写英文字母和（或）数字。
#
# https://leetcode.cn/problems/second-largest-digit-in-a-string
#




from typing import List
import heapq

class Solution:
    def secondHighest(self, s: str) -> int:
        set_num = set()
        heap = []
        for ss in s:
            if not ss.isdigit():
                continue
            i = int(ss)
            if i in set_num:
                continue
            set_num.add(i)
            heapq.heappush(heap, i)
        if len(heap) <= 1:
            return -1
        return heapq.nlargest(2, heap)[1]

so = Solution()

print(so.secondHighest("dfa12321afd"))
print(so.secondHighest("abc1111"))




