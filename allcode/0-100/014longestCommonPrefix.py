# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串""。
#
#
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
# 提示：
#
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        if 0 == N: return ''
        minLen = len(strs[0])
        for s in strs[1:]:
            minLen = min(len(s), minLen)
        # minLen = min([len(s) for s in strs])
        for i in range(minLen):
            for j in range(1, N):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:minLen]


so = Solution()
print(so.longestCommonPrefix([]))
print(so.longestCommonPrefix(["flower","flow","flight"]))   # 'fl'
print(so.longestCommonPrefix(["dog","racecar","car"]))  # ''
