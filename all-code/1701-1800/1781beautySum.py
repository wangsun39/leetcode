# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
#
# 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
# 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
#
#
#
# 示例 1：
#
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
# 示例 2：
#
# 输入：s = "aabcbaa"
# 输出：17
#
#
# 提示：
#
# 1 <= s.length <= 500
# s 只包含小写英文字母。




from typing import List
from collections import defaultdict
from math import inf

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        # print(su)
        ans = 0

        for i in range(n):
            counter = defaultdict(int)  # 字母次数的计数，如counter[2] = 3， 表示出现2次的字母有 3 个
            su = defaultdict(int)  # 前缀和
            su[s[i]] = 1
            counter[1] = 1
            mi = mx = 1
            for j in range(i + 1, n):
                c = su[s[j]]
                su[s[j]] += 1
                if c == 0:
                    mi = 1
                else:
                    if mi == c and counter[mi] == 1:
                        mi += 1
                    if mx == c:
                        mx += 1
                counter[c] -= 1
                counter[c + 1] += 1
                ans += (mx - mi)
        return ans

so = Solution()
print(so.beautySum("aabcb"))  # 5
print(so.beautySum("aabcbaa"))  # 17
print(so.beautySum("pljl"))  # 2
print(so.beautySum("pgljlqegfyqhs"))  # 36




