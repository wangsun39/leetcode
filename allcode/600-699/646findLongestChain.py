# 给出n个数对。在每一个数对中，第一个数字总是比第二个数字小。
#
# 现在，我们定义一种跟随关系，当且仅当b < c时，数对(c, d)才可以跟在(a, b)后面。我们用这种形式来构造一个数对链。
#
# 给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
#
#
#
# 示例：
#
# 输入：[[1,2], [2,3], [3,4]]
# 输出：2
# 解释：最长的数对链是 [1,2] -> [3,4]
#
#
# 提示：
#
# 给出数对的个数在[1, 1000] 范围内。


from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x:[x[1],x[0]])
        dp = [[pairs[i][1], 1] for i in range(n)]  # [rightVal, maxNum]
        for i in range(n):
            mr, mnum = dp[i]
            for j in range(i):
                if pairs[i][0] > dp[j][0]:
                    if dp[j][1] + 1 > mnum:
                        mnum = dp[j][1] + 1
                        mr = pairs[i][1]

            dp[i] = [mr, mnum]

        return max(dp[i][1] for i in range(n))



so = Solution()
print(so.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]))
print(so.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
print(so.findLongestChain([[1,2], [2,3], [3,4]]))

